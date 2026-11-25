import sqlite3
import csv

conexao = sqlite3.connect("minha_conexao")
cursor = conexao.cursor()

query_criacao = '''
CREATE TABLE IF NOT EXISTS acidentes_czech (
    id PRIMARY KEY,
    communication_kind TEXT,
    date TEXT,
    time INT,
    accident_kind TEXT,
    crash_kind TEXT,
    fixed_precaution_kind TEXT,
    injury INT,
    cause_of_accident TEXT,
    alcohol TEXT,
    main_cause_of_accident TEXT,
    killed_persons INT,
    severely_injured INT,
    slightly_injured_person INT,
    total_material_damage INT,
    road_surface_type TEXT,
    condition_of_vehicle_surface TEXT,
    condition_of_communication TEXT,
    weather_conditions TEXT,
    visibility TEXT,
    communication_division TEXT,
    communication_accident_situation TEXT,
    traffic_control_at_the_time_of_accident TEXT,
    specific_location_and_objects_in_the_location_of_the_accident TEXT,
    direction_rates TEXT,
    number_of_vehicles_involved INT,
    location_of_the_traffic_accident TEXT,
    vehicle_type TEXT,
    vehicle_brand TEXT,
    year_of_manufacture INT,
    vehicle_owner TEXT,
    skid TEXT,
    vehicle_sequel TEXT,
    leakage_of_transported_materials TEXT,
    way_of_releasing_persons_from_the_vehicle TEXT,
    direction_of_movement TEXT,
    damage_to_the_vehicle(in_hundred_crowns) INT,
    driver_category TEXT,
    driver_condition TEXT,
    driver_external_influence TEXT,
    city TEXT,
    street TEXT,
    road_type TEXT,
    location TEXT
);
'''
cursor.execute(query_criacao)

with open('C:\\Users\\discente\\Downloads\\bdd2\\bases\\road_accidents_czechia_2016_2022.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    query_insercao = '''
    INSERT INTO acidentes_czech (
        id,
        communication_kind,
        date,
        time,
        accident_kind,
        crash_kind,
        fixed_precaution_kind,
        injury,
        cause_of_accident,
        alcohol,
        main_cause_of_accident,
        killed_persons,
        severely_injured,
        slightly_injured_person,
        total_material_damage,
        road_surface_type,
        condition_of_vehicle_surface,
        condition_of_communication,
        weather_conditions,
        visibility,
        communication_division,
        communication_accident_situation,
        traffic_control_at_the_time_of_accident,
        specific_location_and_objects_in_the_location_of_the_accident,
        direction_pates,
        number_of_vehicles_involved,
        location_of_the_traffic_accident,
        vehicle_type,
        vehicle_brand,
        year_of_manufacture,
        vehicle_owner,
        skid,
        vehicle_sequel,
        leakage_of_transported_materials,
        way_of_releasing_persons_from_the_vehicle,
        direction_of_movement,
        "damage_to_the_vehicle(in_hundred_crowns)",
        driver_category,
        driver_condition,
        driver_external_influence,
        city,
        street,
        road_type,
        location
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    cursor.executemany(query_insercao, leitor_csv)

conexao.commit()
conexao.close()

