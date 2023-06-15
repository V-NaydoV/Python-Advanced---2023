def sorting_cheeses(**cheeses):
    result = ''
    sorted_cheeses = sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantity in sorted_cheeses:
        result += f"{cheese}\n"
        sorted_quantity = sorted(quantity, reverse=True)
        for q in sorted_quantity:
            result += f'{q}\n'
    return result


print(sorting_cheeses(Parmigiano=[165, 215],Feta=[150, 515],Brie=[150, 125]))
