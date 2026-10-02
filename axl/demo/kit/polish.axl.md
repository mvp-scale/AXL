# polish
```axl
word: polish
rules:
  - text:* axl:distinct-font-sizes <= 6
  - text:body font-size >= 16px
  - aria:textbox font-size >= 16px @media:narrow
  - text:body line-height >= 1.5
  - aria:heading line-height <= 1.2
  - page axl:spacing-off-scale == 0 base=4
  - ui:icon axl:emoji-as-icons == 0
  - aria:button wcag:2.5.8 pass
  - text:* wcag:1.4.3 pass
  - state:focus-visible outline-style !contains none
  - aria:heading text-transform == none
  - aria:img lighthouse:unsized-images pass
  - state:invalid ask "Does every error say what went wrong and how to fix it?"
```
