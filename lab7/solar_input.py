from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) != 0 and line[0] != '#':
              object_type = line.split()[0].lower()
              if object_type == "star":  # FIXME: do the same for planet(done)
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
              elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
              else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.R = int(line.split()[1].lower())
    star.color = line.split()[2].lower()
    star.m = int(line.split()[3].lower())
    star.x = int(line.split()[4].lower())
    star.y = int(line.split()[5].lower())
    star.Vx = float(line.split()[6].lower())
    star.Vy = float(line.split()[7].lower())

    

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R = int(line.split()[1].lower())
    planet.color = line.split()[2].lower()
    planet.m = int(line.split()[3].lower())
    planet.x = int(line.split()[4].lower())
    planet.y = int(line.split()[5].lower())
    planet.Vx = float(line.split()[6].lower())
    planet.Vy = float(line.split()[7].lower())


def write_space_objects_data_to_file(space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open('output.txt', 'w') as out_file:
        for obj in space_objects:
          if isinstance(obj, Star):
            out_file.write('Star ' + str(int(obj.R)) + ' ' + str(obj.color) + ' ' + str(int(obj.m)) + ' ' + str(int(obj.x)) + ' ' + str(int(obj.y)) + ' ' + str(int(obj.Vx)) + ' ' + str(int(obj.Vy)) + '\n')
          if isinstance(obj, Planet):
            out_file.write('Planet ' + str(int(obj.R)) + ' ' + str(obj.color) + ' ' + str(int(obj.m)) + ' ' + str(int(obj.x)) + ' ' + str(int(obj.y)) + ' ' + str(int(obj.Vx)) + ' ' + str(int(obj.Vy)) + '\n')
    out_file.close()

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")