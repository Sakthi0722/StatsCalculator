from Statistics.Margin_Error import margin_error


def samp_size(data):
    z = 1.96
    z2 = 0.475
    e = margin_error(data)
    e2 = e / 2
    p = 0.5
    q = 1 - p

    d1 = p * q
    d2 = z2 / e2
    d3 = d2 * d2
    sam = d1 * d3
    return sam
