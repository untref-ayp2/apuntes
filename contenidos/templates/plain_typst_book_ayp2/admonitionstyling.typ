#let breakable_admonitions = true

#let admonition-colors = (
  note: rgb(220, 235, 255),
  tip:  rgb(220, 255, 220),
  warning: rgb("#ef2e02"),
  important: rgb("#11d466"),
  caution:  rgb(255, 235, 180),
)

#let admonition-titles = (
  note: "Note",
  tip: "Tip",
  warning: "Warning",
  important: "Important",
  caution: "Caution",
)

#let admonition-icons = (
  note: "📝",
  tip: "💡",
  warning: "⚠️",
  important: "❗",
  caution: "🚧",
  danger: "🔥",
)

#let admonition(body, kind: "note", title: none, icon: none) = {
  let bg = admonition-colors.at(kind, default: luma(240))
  let heading = if title != none { title } else { admonition-titles.at(kind, default: kind) }

  block(
    breakable: breakable_admonitions,
    stroke: 0.5pt + gray,
    inset: 8pt,
    fill: bg,
    radius: 4pt,
  )[
    #block(inset: 4pt)[
      #text(10pt, strong(heading))
    ]
    #body
  ]
}

#let note(body, title: none, icon: none) = admonition(body, kind: "note", title: title, icon: icon)
#let tip(body, title: none, icon: none) = admonition(body, kind: "tip", title: title, icon: icon)
#let warning(body, title: none, icon: none) = admonition(body, kind: "warning", title: title, icon: icon)
#let important(body, title: none, icon: none) = admonition(body, kind: "important", title: title, icon: icon)
#let caution(body, title: none, icon: none) = admonition(body, kind: "caution", title: title, icon: icon)
