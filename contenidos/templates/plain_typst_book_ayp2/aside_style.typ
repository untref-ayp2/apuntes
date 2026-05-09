#let aside(title, body) = {

    block(
        fill: rgb(244, 147, 147),
        stroke: (left: 1pt + red),
        width: 100%,

        inset: (x: 0.8em, y: 0.4em),
        above: 0.5em,
        below: 0em,

        strong(title)
    )
    block(
        fill: rgb(240, 240, 240),
        stroke: (left: 1pt + red),
        width: 100%,

        inset: (x: 0.8em, y: 0.6em),
        above: 0em,
        below: 0.5em,

        body
    )
}
