from django.contrib import admin
from django.urls import path, include
from .views import home, services, blog, blogitem, thanks, cases, reviews,\
architecture, design_engineering, engineering_projects, planning_approval, real_estate_selection,\
                    rosreestr_approval, rosstroy_approval, boundary_plan, building_and_space_selection,\
                    cadastral_activities, construction_permits, heating_system, land_use_change,\
                    power_supply, ventil_and_air_condit, water_and_sewerage_sys, construction_permits, contacts,\
                    not_found_page, not_found_page, design, repair


handler404 = not_found_page

urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    # path('blog/', blog, name='blog'),
    # path('blogitem/', blogitem, name='blogitem'),
    path('cases/', cases, name='cases'),
    # path('reviews/', reviews, name='reviews'),
    # path('add_reviews/', add_review, name='add_reviews'),
    path('architecture/', architecture, name='architecture'),
    path('construction_permits/', construction_permits, name='construction_permits'),
    path('design_engineering/', design_engineering, name='design_engineering'),
    path('engineering_projects/', engineering_projects, name='engineering_projects'),
    path('planning_approval/', planning_approval, name='planning_approval'),
    path('design/', design, name='design'),
    path('repair/', repair, name='repair'),
    path('real_estate_selection/', real_estate_selection, name='real_estate_selection'),
    path('rosreestr_approval/', rosreestr_approval, name='rosreestr_approval'),
    path('rosstroy_approval/', rosstroy_approval, name='rosstroy_approval'),
    path('boundary_plan/', boundary_plan, name='boundary_plan'),
    path('building_and_space_selection/', building_and_space_selection, name='building_and_space_selection'),
    path('cadastral_activities/', cadastral_activities, name='cadastral_activities'),
    path('construction_permits/', construction_permits, name='construction_permits'),
    path('heating_system/', heating_system, name='heating_system'),
    path('land_use_change/', land_use_change, name='land_use_change'),
    path('power_supply/', power_supply, name='power_supply'),
    path('ventil_and_air_condit/', ventil_and_air_condit, name='ventil_and_air_condit'),
    path('water_and_sewerage_sys/', water_and_sewerage_sys, name='water_and_sewerage_sys'),
    path('contacts/', contacts, name='contacts'),
    path('thanks/', thanks, name='thanks'),
    path('not_found_page/', not_found_page, name='not_found_page'),
    # path('<int: reviews_id>/add_review', add_review, name='add_review')
]
