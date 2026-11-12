# Publicação

Método definido em 12/11/2026:

| Rede | Ferramenta | Conta | ID |
|---|---|---|---|
| Instagram | **Zernio** (conector MCP `mcp.zernio.com/mcp`) | contato.sosseiquefoiassim (nome exibido @sosseiquefoiassim) | `6af5c5457ede50ae7b75574c` |
| TikTok | **Zernio** | @soseiquefoiassimm | `6af5c5547dac04259c95b977` |
| YouTube (Shorts e longos) | **Composio**, conta `youtube_mayo-oscine` (alias `sosei`) | SÓ SEI QUE FOI ASSIM | canal `UCfh_Xgfmf8XSXVZ4MrKSjMQ` |

- Zernio grátis: 2 perfis, posts ilimitados. **Não conectar um 3º perfil no Zernio** (é pago, US$ 6/mês).
- O Buffer conectado ao Claude é do Juro que Explico. **Não usar para o Só Sei.**
- No Composio há duas contas do YouTube. **Sempre passe `account: "youtube_mayo-oscine"`** (a outra, `youtube_housy-wander`, é o Juro que Explico).
- Perfil Zernio: `6af5c519b02f549528da528a`.

## Como agendar (Zernio)
Ferramenta `call_tool` com `name: "posts_create_post"`. Um post por vídeo, com os dois perfis:
- `title`: ID do vídeo (SSA-###)
- `content`: texto do Instagram (`posts.md`, seção Instagram)
- `media_items`: `[{type: video, url: <raw .mp4>, instagramThumbnail: <raw capa.png>}]`
- `platforms`:
  - Instagram: `accountId` do Instagram e `platformSpecificData {shareToFeed: true, instagramThumbnail: <capa>}`
  - TikTok: `accountId` do TikTok e `customContent` com o texto da seção TikTok
- `tiktok_settings`: `{privacyLevel: PUBLIC_TO_EVERYONE, allowComment/allowDuet/allowStitch: true, contentPreviewConfirmed: true, expressConsentGiven: true, videoMadeWithAi: true, commercialContentType: none, videoCoverImageUrl: <capa>}`
- `scheduled_for`: `AAAA-MM-DDTHH:MM:00-03:00`

Antes de agendar, confira que as URLs raw respondem HTTP 200. Um teste com `dry_run: true` valida o TikTok sem publicar.

Depois de agendar, grave o `_id` do post em `agenda.json` (`zernio_post`). Para conferir o resultado, use `posts_get` ou `posts_list status=failed`. Se falhar, use `posts_retry`. Só diga ao fundador que algo foi publicado depois que o status confirmar.

## YouTube (Composio)
A cota de upload do app do Composio é compartilhada com outros usuários e zera às **05:00 de Brasília**. Por isso a rotina diária roda às 05:15 e sobe primeiro o YouTube.

Para cada vídeo pendente no YouTube (ordem: data mais próxima primeiro; só os das próximas 48 h):
1. `COMPOSIO_MULTI_EXECUTE_TOOL` → `YOUTUBE_UPLOAD_VIDEO`, `account: "youtube_mayo-oscine"`, com:
   - `title` e `description`: seção YouTube de `episodios/<ID>/posts.md`
   - `tags`: matéria, "curiosidades", "educação", "só sei que foi assim"
   - `categoryId: "27"`, `privacyStatus: "private"`
   - `videoFilePath: {name: "<ID>.mp4", mimetype: "video/mp4", s3key: "<URL raw do mp4>"}`
2. Com o `videoId` devolvido, `COMPOSIO_PROXY_EXECUTE` (toolkit `youtube`) `PUT https://www.googleapis.com/youtube/v3/videos?part=status` com body `{id, status: {privacyStatus: "private", publishAt: "<data em UTC, ex. 2026-11-13T15:00:00Z>", selfDeclaredMadeForKids: false, containsSyntheticMedia: true}}`. O YouTube publica sozinho na hora marcada.
3. Grave `youtube_video` em `agenda.json` e marque `youtube: "agendado"`.
4. Erro "upload quota exceeded" (400) ou 429: pare, não tente mais vezes no dia. Mande ao fundador o vídeo (`SendUserFile`) e o texto da seção YouTube para ele subir pelo YouTube Studio, e marque `youtube: "manual"`.

Vídeos longos (16:9, ≥ 4 min) sobem pelo mesmo caminho, sem `#shorts` no título. O canal precisa de verificação por telefone para vídeos acima de 15 min.
