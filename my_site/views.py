from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import FormFooterData, FormPopupForm
import logging
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

logger = logging.getLogger(__name__)


def send_data(request):
    form = FormFooterData(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name_under_footer = form.cleaned_data.get('name_under_footer')
        phone_under_footer = form.cleaned_data.get('phone_under_footer')
        message = f'Имя: {name_under_footer}, телефон: {phone_under_footer}'
        try:
            send_mail(
                'Заявка с главной страницы',
                message,
                'soglasovanie-re@yandex.ru',
                ['soglasovanie-re@yandex.ru']
            )
            return redirect('thanks')  # Use the name of the URL that leads to the thank you page
        except Exception as e:
            logger.error(f'Ошибка отправки почты: {e}')
            form.add_error(None, 'Ошибка отправки письма. Попробуйте снова.')
    else:
        form_popup = FormPopupForm()
    return form



def send_data_popup(request):
    if request.method == "POST":
        form_popup = FormPopupForm(request.POST)
        if form_popup.is_valid():
            name_popup = form_popup.cleaned_data.get('name_popup')
            phone_popup = form_popup.cleaned_data.get('phone_popup')
            message = f'Заявка с сайта: Имя: {name_popup}, телефон: {phone_popup}'
            try:
                send_mail(
                    'Заявка с главной страницы',
                    message,
                    'soglasovanie-re@yandex.ru',
                    ['soglasovanie-re@yandex.ru']
                )
                return redirect('thanks')
            except Exception as e:
                logger.error(f'Ошибка отправки почты: {e}')
                form_popup.add_error(None, 'Ошибка отправки письма. Попробуйте снова.')
    else:
        form_popup = FormPopupForm()
    return form_popup


@never_cache
def home(request):
    form = send_data(request) if request.method == "POST" else FormFooterData()
    form_popup = send_data_popup(request)

    if isinstance(form, HttpResponseRedirect):
        return form
    elif isinstance(form_popup, HttpResponseRedirect):
        return form_popup

    return render(request, 'flatpages/additional_pages/index.html', {'form': form, 'form_popup': form_popup})


@never_cache
def services(request):
    return render(request, 'flatpages/additional_pages/services.html')

@never_cache
def blog(request):
    return render(request, 'flatpages/additional_pages/blog.html')

@never_cache
def blogitem(request):
    return render(request, 'flatpages/additional_pages/blogitem.html')

@never_cache
def contacts(request):
    return render(request, 'flatpages/additional_pages/contacts.html')

@never_cache
def thanks(request):
    return render(request, 'flatpages/additional_pages/thanks.html')

@never_cache
def cases(request):
    return render(request, 'flatpages/additional_pages/case.html')

@never_cache
def reviews(request):
    return render(request, 'flatpages/additional_pages/reviews.html')


#services
@never_cache
def architecture(request):
    return render(request, 'flatpages/additional_pages/services/architecture.html')


@never_cache
def design_engineering(request):
    return render(request, 'flatpages/additional_pages/services/design-engineering.html')

@never_cache
def construction_permits(request):
    return render(request, 'flatpages/additional_pages/services/construction-permits.html')

@never_cache
def engineering_projects(request):
    return render(request, 'flatpages/additional_pages/services/engineering-projects.html')


@never_cache
def planning_approval(request):
    return render(request, 'flatpages/additional_pages/services/planning-approval.html')


@never_cache
def real_estate_selection(request):
    return render(request, 'flatpages/additional_pages/services/real-estate-selection.html')

@never_cache
def design(request):
    return render(request, 'flatpages/additional_pages/services/design.html')

@never_cache
def repair(request):
    return render(request, 'flatpages/additional_pages/services/repair.html')


@never_cache
def rosreestr_approval(request):
    return render(request, 'flatpages/additional_pages/services/rosreestr-approval.html')


@never_cache
def rosstroy_approval(request):
    return render(request, 'flatpages/additional_pages/services/rosstroy-approval.html')

#ItemServices
@never_cache
def boundary_plan(request):
    return render(request, 'flatpages/additional_pages/ItemServices/boundary-plan.html')

@never_cache
def building_and_space_selection(request):
    return render(request, 'flatpages/additional_pages/ItemServices/building-and-space-selection.html')

@never_cache
def cadastral_activities(request):
    return render(request, 'flatpages/additional_pages/ItemServices/cadastral-activities.html')

@never_cache
def construction_permits(request):
    return render(request, 'flatpages/additional_pages/ItemServices/construction-permits.html')

@never_cache
def heating_system(request):
    return render(request, 'flatpages/additional_pages/ItemServices/heating-system.html')

@never_cache
def land_use_change(request):
    return render(request, 'flatpages/additional_pages/ItemServices/land-use-change.html')

@never_cache
def power_supply(request):
    return render(request, 'flatpages/additional_pages/ItemServices/power-supply.html')

@never_cache
def ventil_and_air_condit(request):
    return render(request, 'flatpages/additional_pages/ItemServices/ventil-and-air-condit.html')

@never_cache
def water_and_sewerage_sys(request):
    return render(request, 'flatpages/additional_pages/ItemServices/water-and-sewerage-sys.html')

def not_found_page(request, exception):
    return render(request, 'flatpages/additional_pages/not-found-page.html', status=404)
