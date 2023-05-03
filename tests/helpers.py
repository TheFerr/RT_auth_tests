def logger(*args, sep = ' ', end = '\n'):
    """Likewise a print(), but in file log.txt"""
    if args:
        with open('log.txt','a') as logf:
            for arg in args:
                logf.write(str(arg) + sep)
            logf.write(end)

def color_parse(color_in,ret_color='ALL'):
    """Take RGBA format, return R/G/B in 0-255 int A in float 0.0-1.0 ALL in dictionary { 'r':_ 'g':_ 'b':_ 'a':_ } """
    if 'rgba' in color_in:
        r,g,b,a = color_in[5:-1].split(', ')
        ret_color = ret_color.upper()
        if ret_color == 'ALL':
            return { "r":int(r), "g":int(g), "b":int(b), "a":float(a) }
        elif ret_color == 'R':
            return int(r)
        elif ret_color == 'G':
            return int(g)
        elif ret_color == 'B':
            return int(b)
        elif ret_color == 'A':
            return float(a)

def get_red_color(colorin):
    return color_parse(colorin,'R');

def log_tab_colors(page):
    logger( page.tab_phone.get_css('color'),
           page.tab_mail.get_css('color'),
           page.tab_login.get_css('color'),
           page.tab_ls.get_css('color')
           )
