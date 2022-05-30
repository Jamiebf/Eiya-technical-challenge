from flask import jsonify
from sqlalchemy import true
from indexModels import Vehicle
from config import db
import json

def insertVehicle(data):
    try:
        vehicle = Vehicle(
            cities_id = data['cities_id'],
            consume = data['consume'],
            distance = data['distance'],
            consumed = data['consumed']
        )

        db.session.add(vehicle)
        db.session.commit()
        
        return True
    except:
        return False

def listVehicles():
    vehicles = Vehicle.query.all()
    listVehicle = []
    for vehicle in vehicles:
        element = {
        'id' : vehicle.id,
        'cities_id' : {
            'id' : vehicle.city.id,
            'name' : vehicle.city.name,
            'configuration_id' : vehicle.city.configuration_id
            },
        'consume' : vehicle.consume,
        'distance' : vehicle.distance,
        'consumed' : vehicle.consumed
        }

        listVehicle.append(element)
    return jsonify(listVehicle), 200


def deleteVehicleService(id):
    try:
        Vehicle.query.filter_by(id = id).delete()
        db.session.commit()
        return True
    except:
        return False

def patchVehicle(id, body):
    updatedVehicle = Vehicle.query.filter_by(id = id).update(
        body
    ) 
    db.session.commit()
    vehicleQuery = Vehicle.query.filter_by(id = id).first()

    resultVehicle = {
        'id' : vehicleQuery.id,
        'cities_id' : vehicleQuery.cities_id,
        'consume' : vehicleQuery.consume,
        'distance' : vehicleQuery.distance,
        'consumed' : vehicleQuery.consumed
    }
    
    return jsonify(resultVehicle), 200

def verifyData(consume, distance, consumed):
    if (distance/consume) == consumed:
        return True
    else:
        return False

def updateVehicle(vehicle_id, distance_final, consumed_final):
    vehicle = Vehicle.query.filter_by(id = vehicle_id).update(
        {
            "distance": distance_final,
            "consumed": consumed_final
        }
    ) 
    db.session.commit()
    vehicleQuery = Vehicle.query.filter_by(id = vehicle_id).first()

    resultVehicle = {
        'id' : vehicleQuery.id,
        'cities_id' : vehicleQuery.cities_id,
        'consume' : vehicleQuery.consume,
        'distance' : vehicleQuery.distance,
        'consumed' : vehicleQuery.consumed
    }

    return jsonify(resultVehicle), 200




