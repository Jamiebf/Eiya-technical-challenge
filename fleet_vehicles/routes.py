from crypt import methods
from config import app
from Routes import(vehicleRoutes)

app.add_url_rule('/vehicle', view_func= vehicleRoutes.createVehicle, methods = ['POST'])
app.add_url_rule('/vehicle/<id>', view_func= vehicleRoutes.deleteVehicle, methods = ['DELETE'])
app.add_url_rule('/vehicle/<id>', view_func= vehicleRoutes.changeVehicle, methods = ['PATCH'])
app.add_url_rule('/vehicle', view_func= vehicleRoutes.getVehicles, methods = ['GET'])
app.add_url_rule('/travel/<vehicle_id>/<city_id>', view_func= vehicleRoutes.assignTrip, methods = ['PATCH'])