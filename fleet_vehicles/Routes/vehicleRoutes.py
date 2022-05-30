from config import request, jsonify, db
from indexModels import Vehicle, City_cfg
from Service import vehicleService

#Service to create a vehicle
def createVehicle():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({'status': 'failed', 'msg': 'Missing body'}), 400
    except:
        return jsonify({'status': 'failed', 'msg': 'Missing body'}), 400
    
    consume = data['consume']
    distance = data['distance']
    consumed = data['consumed']

    if consumed != 0:
        verify_data_calculations = vehicleService.verifyData(consume,distance,consumed)
        if verify_data_calculations == False:
            return jsonify({'status': 'failed', 'msg': 'The data: consume, distance and consumed do not match. Because you are creating the vehicle the division between distance and consume must be equal to consumed.'}),400
        
    response = vehicleService.insertVehicle(data)
    if response:
        return jsonify({'status': 'successful', 'msg': 'vehicle registered'}), 201
    return jsonify({'status': 'failed', 'msg': 'Something happened'}), 500

#Service to delete vehicle
def deleteVehicle(id):
    verify_vehicle = Vehicle.query.filter_by(id = id).first()
    if not verify_vehicle:
        return jsonify({'status': 'failed', 'msg': 'Vehicle not found'}), 400
    
    response = vehicleService.deleteVehicleService(id)
    if response:
        return jsonify({'status': 'successful', 'msg': 'Vehicle deleted'}), 200
    return jsonify({'status': 'failed', 'msg': 'Something happened'}), 500

#Service to update vehicle
def changeVehicle(id):
    verify_vehicle = Vehicle.query.filter_by(id = id).first()
    if not verify_vehicle:
        return jsonify({'status': 'failed', 'msg': 'Vehicle not found'}), 400
    
    try:
        body = request.get_json(force=True)
        if not body:
            return jsonify({'status':'failed', 'msg': 'Missing body'}), 400
    except:
        return jsonify({'status':'failed', 'msg': 'Missing body'}), 400
    
    body.pop('id', None)

    response = vehicleService.patchVehicle(id,body)
    if response:
        return response
    return jsonify({'status': 'failed', 'msg': 'Something happened'}), 500

def getVehicles():
    response = vehicleService.listVehicles()
    if response:
        return response
    return jsonify({'status': 'failed', 'msg': 'Something happened'}), 500

def assignTrip(vehicle_id, city_id):
    verify_vehicle = Vehicle.query.filter_by(id = vehicle_id).first()
    if not verify_vehicle:
        return jsonify({'status': 'failed', 'msg': 'Vehicle not found'}), 400
 
    current_city = verify_vehicle.cities_id
    city_config = City_cfg.query.filter_by(id = current_city).first()
    if int(city_id) == 1:
        distance = city_config.city_a
    elif int(city_id) == 2:
        distance = city_config.city_b
    else:
        distance = city_config.city_c
    
    distance_final = verify_vehicle.distance + distance
    consume_distance = distance/verify_vehicle.consume
    consumed_final = verify_vehicle.consumed + consume_distance

    response = vehicleService.updateVehicle(vehicle_id, distance_final, consumed_final)
    if response:
        return response
    return jsonify({'status': 'failed', 'msg': 'Something happened'}), 500
    

