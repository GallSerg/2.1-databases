from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def home_view(request):
    template_name = 'calculator/home.html'
    return render(request, template_name)


def rec_show(request, recipe):
    quantity = request.GET.get("servings", 1)
    if recipe in DATA:
        context = {
            'recipe': {k: v*float(quantity) for k, v in DATA[recipe].items()}
        }
        return render(request, 'calculator/index.html', context)
    else:
        context = {}
        return render(request, 'calculator/index.html', context)
