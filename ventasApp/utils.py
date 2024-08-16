
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
#from django.http import HttpResponse

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src) #esto es html
    html = template.render(context_dict) #html bien estructurado
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return result.getvalue()
        #return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None