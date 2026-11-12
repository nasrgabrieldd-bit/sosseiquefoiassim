# Publicação

Método definido em 12/11/2026:

| Rede | Ferramenta | Conta | ID |
|---|---|---|---|
| Instagram | **Zernio** (conector MCP `mcp.zernio.com/mcp`) | contato.sosseiquefoiassim (nome exibido @sosseiquefoiassim) | `6af5c5457ede50ae7b75574c` |
| TikTok | **Zernio** | @soseiquefoiassimm | `6af5c5547dac04259c95b977` |
| YouTube Shorts | **Composio** (2ª conta do app YouTube), a conectar | SÓ SEI QUE FOI ASSIM | a definir |

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

## YouTube
Até o Composio estar ligado ao canal do Só Sei, a rotina diária manda ao fundador o vídeo e o texto da seção YouTube de `posts.md` para ele subir à mão.
Regras de upload: Shorts (vertical, ≤ 3 min), categoria 27 Educação, `madeForKids: false`, divulgação de conteúdo sintético quando couber.
