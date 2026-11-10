// Formatting is used for the owner's readable HTML export, not the minified response.
// Inline text and elements stay together so brand names and sentences keep their spacing.
export function readableHtml(source) {
  const blocks = new Set('html head body header nav main aside section div p h1 h2 h3 h4 dl dt dd ol ul li details summary footer dialog figure figcaption blockquote'.split(' '));
  const single = new Set(['meta', 'link', '!doctype']);
  const tokens = source.match(/<!--[^]*?-->|<script\b[^>]*>[^]*?<\/script>|<[^>]+>|[^<]+/gi) || [];
  const lines = [];
  let current = '';
  let depth = 0;
  const flush = () => {
    if (current.trim()) lines.push('  '.repeat(Math.max(0, depth)) + current.trim());
    current = '';
  };
  for (const token of tokens) {
    const tag = token.match(/^<(\/)?([!\w-]+)/);
    const name = tag?.[2].toLowerCase();
    if (name === 'script') { flush(); current = token; flush(); continue; }
    if (blocks.has(name)) {
      flush();
      if (tag[1]) depth = Math.max(0, depth - 1);
      current = token;
      flush();
      if (!tag[1]) depth++;
    } else if (single.has(name)) {
      flush(); current = token; flush();
    } else current += token;
  }
  flush();
  return lines.join('\n') + '\n';
}
