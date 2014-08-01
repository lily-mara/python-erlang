def extended_b_lines(bht, blocking):
    line_count = 1
    while extended_b(bht, line_count) > blocking:
        line_count += 1
    return line_count


def extended_b(traffic, lines, recall=0.5):
    original_traffic = traffic
    while True:
        PB = b(traffic, lines)
        magic_number_1 = (1 - PB) * traffic + (1 - recall) * PB * traffic
        magic_number_2 = 0.9999 * original_traffic
        if magic_number_1 >= magic_number_2:
            return PB
        traffic = original_traffic + recall * PB * traffic
    return -1


def b(traffic, lines):
    if traffic > 0:
        PBR = (1 + traffic) / traffic
        for index in range(2, lines + 1):
            PBR = index / traffic * PBR + 1
            if PBR > 10000:
                return 0
        return 1 / PBR
    return 0
