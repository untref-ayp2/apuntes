#let leftCaption(it) = {
  set text(size: 8pt)
  set align(left)
  set par(justify: true)

  context(it, {
    text(weight: "bold")[#it.supplement #it.counter.display(it.numbering).]
  })

  h(4pt)
  set text(fill: black.lighten(20%), style: "italic")
  it.body
}


#let template(
  // FRONTPAGE.
  title: "Apuntes de Algoritmos y Programación II",
  subtitle: "Ingeniería en Computación",
  authors: "Cátedra de Algoritmos y Programación II",
  cover: "untref-logo.svg",
  cover_width: 12cm,
  coverposition: 1cm,
  justification: true,

  // TOC
  ToC_depth: 3,
  show_ToC: true,

  // PREFACE
  preface: none,

  // SPECIFICATION of output
  paper-size: "a4",
  margin: (),
  linespacing: .65em,
  show_pagenumber: true,
  margin_top: 2.5cm,
  margin_bottom: 2.5cm,
  margin_left: 3cm,
  margin_right: 2cm,
  logo: none,
  logo_width: 10%,

  font: ("Roboto", "Noto Color Emoji"),
  fontsize: 11pt,

  theme: blue.darken(30%),
  colorheadings: blue.darken(30%),

  // The book's content.
  body
) = {

  set page(
    numbering: none,
    paper-size,
    )

  set heading(numbering: (..args) => {
    let nums = args.pos()
    let level = nums.len()
    if level == 1 {[#numbering("1.", ..nums)]} else {[#numbering("1.1.1", ..nums)]}
    },

)

  set figure(numbering: (..args) => {
    let chapter = counter(heading).display((..nums) => nums.pos().at(0))
    let fig = counter(figure).display("1")
    [#chapter.#fig]
  })


  // Configure equation numbering and spacing.
  set math.equation(numbering: (..args) => {
    let chapter = counter(heading).display((..nums) => nums.pos().at(0))
    [(#chapter.#numbering("1", ..args.pos()))]
  })
  show math.equation: set block(spacing: 1em)


  // Configure lists.
  set enum(indent: 10pt, body-indent: 9pt)
  set list(indent: 10pt, body-indent: 9pt)



// COVERPAGE
  align(center,
    block(
      fill: theme,
      inset: 20pt,
      radius: 4pt,
      width: 80%,
      text(24pt, weight: "bold", fill: white, title)
    )
  )

  if subtitle != none {
    v(1em)
    align(center, text(16pt, fill: gray.darken(30%), weight: "semibold", subtitle))
  }

  if cover != none {
    v(coverposition)
    align(center, image((cover), width: cover_width))
  }

  v(1em)

  if authors != none {
    place(bottom + center,
      text(14pt, fill: gray.darken(50%), weight: "medium", authors)
    )
  }


// PREFACE
  if preface != none {
    pagebreak()
    place(top + left,
      text(18pt, fill: theme, weight: "bold", "Prefacio")
    )
    v(2em)
    set par(justify: true)
    align(left, box(width: 100%, text(11pt, font: "Roboto", fill: gray.darken(30%), preface)))
  }


//OUTLINE OF THE BOOK
  pagebreak()
  if show_ToC == true {

    show outline.entry.where(level: 1): it => {
      v(15pt, weak: true)
      text(weight: "bold", size: 11pt, fill: theme, it)
    }

    show outline.entry.where(level: 2): it => {
      text(size: 10pt, it)
    }

    text(size: 20pt, weight: "bold", fill: theme, "Índice")
    v(1em)
    line(length: 100%, stroke: 2pt + theme)
    v(1em)
    outline(
      title: none,
      depth: ToC_depth,
      indent: 1.5em,
    )
  }

//RESETING NUMBERING AND CHAPTER STYLING
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    counter(figure).update(0)
    counter(figure.where(kind: table)).update(0)
    counter(math.equation).update(0)

    v(3em)

    block(
      fill: theme,
      inset: (x: 20pt, y: 15pt),
      radius: 0pt,
      width: 100%,
      {
        text(size: 32pt, weight: "bold", fill: white, it)
      }
    )

    v(2em)
  }

  show heading.where(level: 2): it => {
    v(1.8em)

    place(
      left,
      dx: -2.5cm,
      text(size: 16pt, weight: "bold", fill: theme)[
        #counter(heading).display()
      ]
    )

    text(size: 16pt, weight: "bold", it.body)
    v(0.5em)
    line(length: 40%, stroke: 1pt + theme.lighten(40%))
    v(1.2em)
  }

  show heading.where(level: 3): it => {
    v(1.5em)

    box(width: 3pt, height: 1em, fill: theme, radius: 1pt)
    h(6pt)
    text(size: 13pt, weight: "semibold", fill: theme.darken(10%), it.body)
    v(0.8em)
  }

  show heading.where(level: 4): set text(colorheadings, size: 11pt, weight: "semibold")
  show heading.where(level: 5): set text(colorheadings, size: 10pt, weight: "semibold")


// PAGE LAY OUT OF CONTENT
  set page(
    numbering: if show_pagenumber == true {"1"} else {none},
    footer: context [
      #line(length: 100%, stroke: 0.5pt + theme.lighten(60%))
      #v(0.4em)
      #grid(
        columns: (1fr, auto, 1fr),
        align: (left, center, right),
        [
          #text(size: 9pt, fill: gray.darken(20%), style: "italic")[
            #context {
              let headings = query(selector(heading.where(level: 1)).before(here()))
              if headings.len() > 0 {
                let last-heading = headings.last()
                last-heading.body
              }
            }
          ]
        ],
        [],
        [
          #if show_pagenumber {
            box(
              fill: theme,
              inset: (x: 8pt, y: 4pt),
              radius: 3pt,
              text(size: 9pt, fill: white, weight: "bold")[#counter(page).display("1")]
            )
          }
        ]
      )
    ],
    margin: (
      top: margin_top,
      bottom: margin_bottom,
      left: margin_left,
      right: margin_right
    ),
    header: if logo != none {
      v(0.5em)
      line(length: 100%, stroke: 0.5pt + theme.lighten(60%))
      v(0.3em)
      align(center)[#image(logo, width: logo_width)]
      v(0.3em)
      line(length: 100%, stroke: 0.5pt + theme.lighten(60%))
    } else { none },
  )

  set text(
    font: font,
    size: fontsize
  )
  set par(
    leading: linespacing,
    justify: justification
  )

  counter(page).update(1)

  // Code block styling
  show raw.where(block: true): it => {
    let lang = if it.has("lang") { it.lang } else { none }
    let title = if lang != none {
      if lang == "python" { "Python" }
      else if lang == "go" or lang == "golang" { "Go" }
      else if lang == "rust" { "Rust" }
      else if lang == "cpp" { "C++" }
      else if lang == "c" { "C" }
      else if lang == "java" { "Java" }
      else if lang == "js" or lang == "javascript" { "JavaScript" }
      else if lang == "ts" or lang == "typescript" { "TypeScript" }
      else if lang == "html" { "HTML" }
      else if lang == "css" { "CSS" }
      else if lang == "sql" { "SQL" }
      else if lang == "bash" or lang == "sh" { "Shell" }
      else if lang == "json" { "JSON" }
      else if lang == "yaml" or lang == "yml" { "YAML" }
      else if lang == "xml" { "XML" }
      else if lang == "typ" or lang == "typst" { "Typst" }
      else { lang }
    } else { none }

    block(
      fill: luma(245),
      inset: 0pt,
      radius: 3pt,
      stroke: 0.5pt + theme.lighten(60%),
      width: 100%,
      clip: true,
      {
        if title != none {
          block(
            fill: theme.lighten(85%),
            width: 100%,
            inset: (x: 12pt, y: 8pt),
            stroke: (bottom: 0.5pt + theme.lighten(50%)),
            text(weight: "bold", fill: theme.darken(10%), font: "Roboto", size: 9pt, title)
          )
        }
        block(
          inset: 12pt,
          width: 100%,
          text(font: "DejaVu Sans Mono", size: 8.5pt, it)
        )
      }
    )
  }

  // Style for admonitions
  show figure.where(kind: "admonition"): it => {
    block(
      fill: theme.lighten(90%),
      stroke: (left: 3pt + theme),
      radius: 2pt,
      inset: 12pt,
      width: 100%,
      [
        #text(weight: "bold", fill: theme, size: 10pt)[#it.caption]
        #v(0.5em)
        #it.body
      ]
    )
  }

  [#body]
}
