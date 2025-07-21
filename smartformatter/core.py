
import re
import inflect

def formate_name(name):
    return ' '.join([w.capitatalize() for w in name.strip().split()])

def format_phone(phone):
    digits = re.sun(r'\D','', phone)
    return f"+{digits[:2]} {digits[2:7]} {digits[7:]}"

def format_currency(amount, symbol='$')
    return f"{symbol}{amount:,.2f}"

def number_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n).replace(',', '')

def slugify(text)
   return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
