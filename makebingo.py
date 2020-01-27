#!/usr/bin/env python3

import argparse
import math
import random
import cairo


WIDTH = 8.5 * 72
HEIGHT = 11 * 72

XMARGIN = 10
YMARGIN = 10

BOXMARGIN = 6
BOXBORDER = 3
BOXSIZE = ((WIDTH - (2 * XMARGIN)) / 5) - BOXMARGIN


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', type=str)
    args = parser.parse_args()

    try:
        with open(args.data_file, 'r') as fi:
            categories = [next(fi).strip() for i in range(25)]
    except Exception:
        print('There is a problem with the data file')

    random.shuffle(categories)

    pdf = cairo.PDFSurface('test.pdf', WIDTH, HEIGHT)
    context = cairo.Context(pdf)

    context.rectangle(0, 0, WIDTH, HEIGHT)
    context.fill()    

    draw_grid(context, categories)

    context.save()
    context.show_page()
    pdf.finish()


def draw_grid(ctx, categories):
    ypos = YMARGIN

    for i in range(5):
        draw_row(ctx, ypos, categories[i * 5: ((i * 5) + 5)])
        ypos += BOXSIZE + BOXMARGIN


def draw_row(ctx, ypos, categories):
    xpos = XMARGIN
    print(categories)
    for i in range(5):
        fill = (1, 1, 1)
        draw_square(ctx, xpos, ypos, fill, categories[i])
        xpos += BOXSIZE + BOXMARGIN


def draw_square(ctx, xpos, ypos, fillcolor, category):
    ctx.set_line_width(BOXBORDER)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(xpos, ypos)

    ctx.rectangle(xpos, ypos, BOXSIZE, BOXSIZE)
    ctx.stroke_preserve()

    ctx.set_source_rgb(*fillcolor)
    ctx.fill()

    write_text(ctx, xpos, ypos, category)


def write_text(ctx, xpos, ypos, text):
    ctx.set_source_rgb(0, 0, 0)

    lines = split_text(ctx, text)
    line_count = len(lines)
    
    print('Considering:', text)
    print('Text length:', len(text))
    print('Line Count:', line_count)
    print('Split:', lines)

    if line_count % 2 == 0:
        for i, line_text in enumerate(lines):
            line_width, line_height = text_size(ctx, line_text)
            ctx.move_to(
                xpos + (BOXSIZE / 2) - (line_width / 2),
                ypos + (BOXSIZE / 2) - ((line_count * line_height) / 2) + (i * line_height) + (line_height / 2))
            ctx.show_text(line_text)
    else:
        for i, line_text in enumerate(lines):
            line_width, line_height = text_size(ctx, line_text)
            ctx.move_to(
                xpos + (BOXSIZE / 2) - (line_width / 2),
                ypos + (BOXSIZE / 2) - (((line_count - 1) * line_height) / 2) + (i * line_height))
            ctx.show_text(line_text)


def split_text(ctx, text):
    w, h = text_size(ctx, text)
    line_count = math.ceil(w / BOXSIZE)
    chars_per_line = math.ceil(len(text) / line_count)
    lines = list()

    if len(text) <= chars_per_line:
        return [text]

    while True:
        offset = 0
        while text[chars_per_line + offset] != ' ':
            offset -= 1
            
            if offset + chars_per_line == 0:
                offset = 0
                break

        lines.append(text[:(chars_per_line + offset)].strip())
        text = text[chars_per_line + offset:].strip()

        if len(text) <= chars_per_line:
            if len(text) == 0:
                break
            lines.append(text)
            break

    return lines


def text_size(ctx, text):
    _, _, width, height, _, _ = ctx.text_extents(text)
    return width, height


if __name__ == '__main__':
    main()
