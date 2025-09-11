1️⃣ Login via API Key

Endpoint: POST /login_apikey

Fluxo:

O cliente envia a API Key no header: x-api-key: <API_KEY>.

O Depends(get_current_client) valida se a API Key está na lista VALID_API_KEYS.

Se inválida → retorna 401 Unauthorized.

Se válida → o backend gera:

Access Token (create_access_token) → válido por ACCESS_TOKEN_EXPIRE_MINUTES (atualmente 7 dias no seu settings, mas você comentou que quer 1 hora).

Refresh Token (create_refresh_token) → válido por REFRESH_TOKEN_EXPIRE_DAYS (configurado como 7 dias).

Retorna JSON:

{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}


💡 Resumo: Aqui você troca uma API Key estática por tokens JWT que expiram, garantindo mais segurança.

2️⃣ Usando o Access Token

Endpoints protegidos, exemplo: GET /me

Fluxo:

O cliente envia header: Authorization: Bearer <ACCESS_TOKEN>.

O Depends(get_current_user_from_jwt) decodifica o token:

Verifica assinatura e validade (jwt.decode).

Confirma que existe o campo sub → identifica o cliente.

Se o token for válido → retorna os dados protegidos.

Se o token expirar ou for inválido → retorna 401 Unauthorized.

💡 Resumo: O Access Token é usado para autenticar requisições até expirar. Depois disso, o cliente precisa de um novo token.

3️⃣ Refresh Token

Endpoint: POST /refresh_apikey

Fluxo:

O cliente envia o Refresh Token via header Authorization: Bearer <REFRESH_TOKEN>.

O backend decodifica o token:

Verifica assinatura e validade.

Confirma que o type é "refresh_token" (não é um access token disfarçado).

Extrai sub do payload.

Se válido → gera novos Access e Refresh Tokens e retorna para o cliente:

{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}


Se inválido → retorna 401 Unauthorized.

💡 Resumo: O Refresh Token permite ao cliente obter novos tokens sem precisar enviar a API Key de novo, mantendo o usuário "logado" de forma segura.

4️⃣ Ciclo de uso típico

App mobile envia API Key → recebe Access + Refresh Token.

App usa Access Token para chamadas protegidas (/me, etc.).

Quando o Access Token expira:

App envia Refresh Token para /refresh_apikey.

Recebe novos Access + Refresh Token.

Quando o Refresh Token expira:

Usuário precisa fazer login novamente usando API Key.