from ngsildclient import Entity, Client, SmartDataModels
import random

AGRIFOOD_CTX = 'https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld'
N_PARCELS = 0
N_FARMS = 0
N_PESTICIDE_APPLICATIONS = 0
N_CROPS = 0

def create_farm(parcels, name):
    
    # Load exmaple model and edit relevant data
    farm = Entity.load(SmartDataModels.SmartAgri.Agrifood.AgriFarm)

    # Provide list of parcel IDs which this farm relates to
    parcel_id_list = list(map(lambda parcel: parcel.id, parcels))
    farm.rel('hasAgriParcel', parcel_id_list)
    farm.prop('name', name)

    global N_FARMS
    N_FARMS += 1
    farm.id = f'urn:ngsi-ld:AgriFarm:Farm-{N_FARMS}'

    farm.pprint()

    return farm


def create_parcel(crop):
    
    # Load exmaple model and edit relevant data
    parcel = Entity.load(SmartDataModels.SmartAgri.Agrifood.AgriParcel)


    global N_PARCELS
    N_PARCELS += 1
    '''
    1. URN - Uniform Resource Name
    2. NGSI-LD 
    3. AgriParcel definition from the Smart Data Initiative
    4. Cutom ID part, usually a UUID (Universally Unique IDentifier) or some kind of date format
    '''
    parcel.id = f'urn:ngsi-ld:AgriParcel:parcel-{N_PARCELS}-id'

    # parcel.landLocation = None
    parcel.prop('location', [])
    parcel.rel('hasAgriCrop', crop.id)

    parcel.pprint()

    return parcel


def create_pesticide_application_event(parcel):

    global N_PESTICIDE_APPLICATIONS
    N_PESTICIDE_APPLICATIONS += 1
    # Load exmaple model and edit relevant data
    pesticideApplication = Entity.load(SmartDataModels.SmartAgri.Agrifood.AgriParcelOperation)

    '''
    1. URN - Uniform Resource Name
    2. NGSI-LD 
    3. AgriParcelOperation definition from the Smart Data Initiative
    4. Cutom ID part, usually a UUID (Universally Unique IDentifier) or some kind of date format
    '''
    pesticideApplication.id = f'urn:ngsi-ld:AgriParcelOperation:{N_PESTICIDE_APPLICATIONS}'
    pesticideApplication.rel('hasAgriParcel', parcel.id)
    pesticideApplication.prop("operationType", f'Pesticide application')
    pesticideApplication.prop("description", f'Regular pesticide application #{N_PESTICIDE_APPLICATIONS}')
    pesticideApplication.prop("quantity", random.randint(1, 10), unitcode="l/ha")

    pesticideApplication.pprint()

    return pesticideApplication


def create_crop(type):

    global N_CROPS
    N_CROPS += 1
    
    # Load exmaple model and edit relevant data
    crop = Entity.load(SmartDataModels.SmartAgri.Agrifood.AgriCrop)

    crop.id = f'urn:ngsi-ld:AgriCrop:crop-{N_CROPS}-id'
    crop.prop('description', type)
    crop.prop('name', type)
    crop.prop('alternateName', f'Scientific name for "{type}"')

    return crop


def register_dt_entity(entity):

    with Client() as client:

        print(f'Inserting entity! [{entity.id}]')
        client.create(entity)


def main():

    wheat_crop_1 = create_crop('wheat')
    soy_crop_1 = create_crop('soy')
    apple_crop_1 = create_crop('apple')

    parcel1 = create_parcel(wheat_crop_1)
    parcel2 = create_parcel(soy_crop_1)
    parcel3 = create_parcel(apple_crop_1)

    farm1 = create_farm([parcel1, parcel2], 'Lithuania')
    farm2 = create_farm([parcel3], 'Spain')

    pesticideApplication1 = create_pesticide_application_event(parcel1)
    pesticideApplication2 = create_pesticide_application_event(parcel3)


    register_dt_entity(farm1)
    register_dt_entity(farm2)
    register_dt_entity(parcel1)
    register_dt_entity(parcel2)
    register_dt_entity(parcel3)
    register_dt_entity(wheat_crop_1)
    register_dt_entity(soy_crop_1)
    register_dt_entity(apple_crop_1)
    register_dt_entity(pesticideApplication1)
    register_dt_entity(pesticideApplication2)


if __name__ == '__main__':
    main()