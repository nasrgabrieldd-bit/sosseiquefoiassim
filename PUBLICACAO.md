# Publicação

Método definido em 12/11/2026:

| Rede | Ferramenta | Conta | ID |
|---|---|---|---|
| Instagram | **Zernio** (conector MCP `mcp.zernio.com/mcp`) | contato.sosseiquefoiassim (nome exibido @sosseiquefoiassim) | `6af5c5457ede50ae7b75574c` |
| TikTok | **Zernio** | @soseiquefoiassimm | `6af5c5547dac04259c95b977` |
| YouTube (Shorts e longos) | **Composio**, conta `youtube_mayo-oscine` (alias `sosei`) | SÓ SEI QUE FOI ASSIM | canal `UCfh_Xgfmf8XSXVZ4MrKSjMQ` |

- Zernio grátis: 2 perfis, posts ilimitados. **Não conectar um 3º perfil no Zernio** (é pago, US$ 6/mês).
- O Buffer conectado ao Claude é do Juro que Explico. **Não usar para o Só Sei.**
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
No Composio há duas contas de YouTube. **Sempre passe `account="sosei"`** e confira se o `channelId` da resposta é `UCfh_Xgfmf8XSXVZ4MrKSjMQ`. A outra conta (`youtube_housy-wander`) é o Juro que Explico.

No workbench (`COMPOSIO_REMOTE_WORKBENCH`):
1. Baixe o mp4 da URL raw do GitHub e rode `upload_local_file(path)` para obter o `s3key`.
2. Rode `YOUTUBE_MULTIPART_UPLOAD_VIDEO` com `{title, description, tags, categoryId: "27", privacyStatus: "private", videoFile: {name, mimetype: "video/mp4", s3key}}` e `account="sosei"`. O ID fica em `data.video.id`. **Não use `YOUTUBE_UPLOAD_VIDEO`:** em 12/11 ele deu `uploadStatus: failed` e o YouTube apagou o vídeo.
3. Rode `proxy_execute('PUT', 'https://www.googleapis.com/youtube/v3/videos', 'youtube', query_params={'part': 'status'}, body={"id": ID, "status": {"privacyStatus": "private", "publishAt": "<UTC>Z", "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True, "embeddable": True, "license": "youtube", "publicStatsViewable": True}})`. Use a URL absoluta: o caminho relativo dá 404. 12:00 em Brasília = 15:00Z; 19:00 = 22:00Z.
4. Confira com GET `videos?part=status&id=...`: `uploadStatus` deve estar `uploaded` ou `processed`, e `publishAt` deve estar preenchido. Grave o `youtube_id` em `agenda.json`.

Regras:
- Na descrição não pode haver `<` nem `>`: o YouTube recusa com "invalid video description". Troque por →.
- **Limite diário de envios do canal:** em 12/11 entraram 8 vídeos e o 9º deu "exceeded the number of videos they may upload". Suba no máximo cerca de 6 por dia e deixe o resto para o dia seguinte. Os 2 vídeos diários da rotina cabem nesse limite.
- **Vídeos longos** (16:9, mais de 3 min) seguem o mesmo caminho; o canal está com `longUploadsStatus: eligible`. Para capa personalizada, use `YOUTUBE_UPDATE_THUMBNAIL`, que exige verificação por telefone do canal.
- Os títulos dos Shorts levam `#shorts`. Os longos, não.
- Use o texto da seção YouTube de `posts.md` (título e descrição); as tags são as hashtags da descrição sem o `#`.
