from IPython.display import HTML, display


def timing_table(values, title="", reference=None):
    """Render a nice HTML timing table"""
    chunks = []
    if title:
        chunks.extend([f"<h3>{title}</h3>", ""])
    if reference is None:
        # reference field is first key by default
        reference = next(iter(values.keys()))

    tr = values[reference]

    chunks.extend(
        [
            f"""<center>
        <table>
        <tr><th>implementation</th><th>speed</th></tr>
        <tr><td>{reference}</td><td>1.0 (normalized)</td></tr>
        """,
        ]
    )
    for key, value in values.items():
        if key == reference:
            continue
        if hasattr(tr, "average"):
            # given TimeitResults, compare averages
            speedup = tr.average / value.average
        else:
            # given floats
            speedup = tr / value
        if speedup < 10:
            speedup = f"{speedup:.2f}x"
        elif speedup < 100:
            speedup = f"{speedup:.1f}x"
        else:
            speedup = f"{speedup:,.0f}x"
        chunks.append(f"<tr><td>{key}</td><td>{speedup}</td></tr>")
    chunks.append("</table></center>")
    display(HTML("\n".join(chunks)))
