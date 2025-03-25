from django import template


register = template.Library()

@register.filter
def format_services(service_list):
    """ Faz a listagem personalizada das especialidades. """
    if not service_list:
        return ""
    
    if len(service_list) == 1:
        return service_list[0]

    return f'{", ".join(service_list[:-1])} e {service_list[-1]}'
