from colorama import Fore, Style, Back

class TextBorder:
    def __init__(self):
        pass


    def single_border(self, text, border_color='', text_color='', bg_color=''):
        lines = text.split('\n')
        width = max(len(s) for s in lines)
        border_color = border_color.upper()
        text_color = text_color.upper()
        bg_color = bg_color.upper()
        if border_color and bg_color:
            border = f'{getattr(Back, bg_color)}{getattr(Fore, border_color)}+{"-" * (width + 2)}+{Style.RESET_ALL}'
            sides = f'{getattr(Back, bg_color)}{getattr(Fore, border_color)}|{Style.RESET_ALL}'
        elif border_color:
            border = f'{getattr(Fore, border_color)}+{"-" * (width + 2)}+{Style.RESET_ALL}'
            sides = f'{getattr(Fore, border_color)}|{Style.RESET_ALL}'
        elif bg_color:
            border = f'{getattr(Back, bg_color)}+{"-" * (width + 2)}+{Style.RESET_ALL}'
            sides = f'{getattr(Back, bg_color)}|{Style.RESET_ALL}'
        else:
            border = '+' + '-' * (width + 2) + '+'
            sides = '|'
        result = [border]
        for line in lines:
            if text_color:
                result.append(f'{sides} {getattr(Fore, text_color)}{line.ljust(width)}{Style.RESET_ALL} {sides}')
            else:
                result.append(f'{sides} {line.ljust(width)} {sides}')
        result.append(border)
        return '\n'.join(result)
    

    def double_border(self, text, border_color='', text_color='', bg_color=''):
        lines = text.split('\n')
        width = max(len(s) for s in lines)
        border_color = border_color.upper()
        text_color = text_color.upper()
        bg_color = bg_color.upper()
        if border_color and bg_color:
            border = f'{getattr(Back, bg_color)}{getattr(Fore, border_color)}#{"=" * (width + 4)}#{Style.RESET_ALL}'
            sides = f'{getattr(Back, bg_color)}{getattr(Fore, border_color)}||{Style.RESET_ALL}'
        elif border_color:
            border = f'{getattr(Fore, border_color)}#{"=" * (width + 4)}#{Style.RESET_ALL}'
            sides = f'{getattr(Fore, border_color)}||{Style.RESET_ALL}'
        elif bg_color:        
            border = f'{getattr(Fore, border_color)}#{"=" * (width + 4)}#{Style.RESET_ALL}'
            sides = f'{getattr(Fore, border_color)}||{Style.RESET_ALL}'
        else:
            border = '#' + '=' * (width + 4) + '#'
            sides = '||'
        result = [border]
        for line in lines:
            if text_color:
                result.append(f'{sides} {getattr(Fore, text_color)}{line.ljust(width)}{Style.RESET_ALL} {sides}')
            else:
                result.append(f'{sides} {line.ljust(width)} {sides}')
        result.append(border)
        return '\n'.join(result)
    

    def dashed_border(self, text, border_color='', text_color='', bg_color=''):
        lines = text.split('\n')
        width = max(len(s) for s in lines)
        border_color = border_color.upper()
        text_color = text_color.upper()
        bg_color = bg_color.upper()
        if border_color and bg_color:
            border = f'{getattr(Back, bg_color)}{getattr(Fore, border_color)}+{"-" * (width + 2)}+{Style.RESET_ALL}'
            sides = f'{getattr(Back, bg_color)}{getattr(Fore, border_color)} |{Style.RESET_ALL}'
        elif border_color:
            border = f'{getattr(Fore, border_color)}+{"-" * (width + 2)}+{Style.RESET_ALL}'
            sides = f'{getattr(Fore, border_color)}|{Style.RESET_ALL}'
        elif bg_color:
            border = f'{getattr(Back, bg_color)}+{"-" * (width + 2)}+{Style.RESET_ALL}'
            sides = f'{getattr(Back, bg_color)}|{Style.RESET_ALL}'
        else:
            border = '+' + '-' * (width + 2) + '+'
            sides = '|'
        lines[0] = lines[0].replace('-', '=')
        lines[-1] = lines[-1].replace('-', '=')
        result = [border]
        for line in lines:
            if text_color:
                result.append(f'{sides} {getattr(Fore, text_color)}{line.ljust(width)}{Style.RESET_ALL}{sides}')
            else:
                result.append(f'{sides} {line.ljust(width)}{sides}')
        result.append(border)
        return '\n'.join(result)
