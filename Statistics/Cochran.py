from Statistics.Margin_Error import margin_error


def cochran(data):
    try:
        e = margin_error(data)
        p = 0.5  # Proportion of population(estimated)
        z = 1.96  # random standard deviation
        q = 1 - p
        s1 = z * z  # squaring
        s2 = p * q
        s3 = s1 * s2
        s4 = e * e  # squaring
        coh = s3 / s4
        return coh
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")