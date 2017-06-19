import io

import boto3
from PIL import Image

import GoogleImageDownloader
from utils.ImageUtils import ImageUtils


class Rekognition:
    def __init__(self):
        self.rekognition_client = boto3.client('rekognition')

    def fetch_image_and_label_it(self, keyword):
        raw_img = GoogleImageDownloader.get_image_from_google(keyword)
        self.detect_labels(raw_img)

    def detect_moderation_labels(self):
        self.rekognition_client.detect_moderation_labels(
        )

    '''
    {
    u'Labels':[
      {
         u'Confidence':98.82992553710938,
         u'Name':u'People'
      },
      {
         u'Confidence':98.82994842529297,
         u'Name':u'Person'
      },
      {
         u'Confidence':98.76869201660156,
         u'Name':u'Human'
      },
      {
         u'Confidence':83.38436126708984,
         u'Name':u'Landslide'
      }
    ],
    'ResponseMetadata':{
      'RetryAttempts':0,
      'HTTPStatusCode':200,
      'RequestId':'53c5a356-3a08-11e7-bb4d-0b9e73be3287',
      'HTTPHeaders':{
         'date':'Tue, 16 May 2017 07:21:52 GMT',
         'x-amzn-requestid':'53c5a356-3a08-11e7-bb4d-0b9e73be3287',
         'content-length':'245',
         'content-type':'application/x-amz-json-1.1',
         'connection':'keep-alive'
      }
    },
    u'OrientationCorrection':u'ROTATE_0'
    }
    '''

    def detect_labels(self, image_raw):
        response = self.rekognition_client.detect_labels(
            Image={
                'Bytes': image_raw
            },
            MaxLabels=123,
            MinConfidence=60
        )  # Let's use Amazon S3
        return response

    '''
    Multiple persons : 
    {  
       u'FaceDetails':[  
          {  
             u'Confidence':99.99884796142578,
             u'Eyeglasses':{  
                u'Confidence':99.99901580810547,
                u'Value':False
             },
             u'Sunglasses':{  
                u'Confidence':99.95965576171875,
                u'Value':False
             },
             u'Gender':{  
                u'Confidence':99.92436218261719,
                u'Value':u'Male'
             },
             u'Landmarks':[  
                {  
                   u'Y':0.13891878724098206,
                   u'X':0.23046399652957916,
                   u'Type':u'eyeLeft'
                },
                {  
                   u'Y':0.1453937143087387,
                   u'X':0.2806556820869446,
                   u'Type':u'eyeRight'
                },
                {  
                   u'Y':0.1793181151151657,
                   u'X':0.2578807771205902,
                   u'Type':u'nose'
                },
                {  
                   u'Y':0.21722586452960968,
                   u'X':0.24002335965633392,
                   u'Type':u'mouthLeft'
                },
                {  
                   u'Y':0.2201988846063614,
                   u'X':0.27420422434806824,
                   u'Type':u'mouthRight'
                },
                {  
                   u'Y':0.13646815717220306,
                   u'X':0.23011301457881927,
                   u'Type':u'leftPupil'
                },
                {  
                   u'Y':0.1475914716720581,
                   u'X':0.28094685077667236,
                   u'Type':u'rightPupil'
                },
                {  
                   u'Y':0.11827725172042847,
                   u'X':0.21111969649791718,
                   u'Type':u'leftEyeBrowLeft'
                },
                {  
                   u'Y':0.11123076826334,
                   u'X':0.22645236551761627,
                   u'Type':u'leftEyeBrowRight'
                },
                {  
                   u'Y':0.11954889446496964,
                   u'X':0.24194593727588654,
                   u'Type':u'leftEyeBrowUp'
                },
                {  
                   u'Y':0.1235363557934761,
                   u'X':0.26833733916282654,
                   u'Type':u'rightEyeBrowLeft'
                },
                {  
                   u'Y':0.12088008970022202,
                   u'X':0.2841956317424774,
                   u'Type':u'rightEyeBrowRight'
                },
                {  
                   u'Y':0.12964500486850739,
                   u'X':0.2989998459815979,
                   u'Type':u'rightEyeBrowUp'
                },
                {  
                   u'Y':0.1383112519979477,
                   u'X':0.22076298296451569,
                   u'Type':u'leftEyeLeft'
                },
                {  
                   u'Y':0.14087218046188354,
                   u'X':0.2402670681476593,
                   u'Type':u'leftEyeRight'
                },
                {  
                   u'Y':0.1334783136844635,
                   u'X':0.23078639805316925,
                   u'Type':u'leftEyeUp'
                },
                {  
                   u'Y':0.14368632435798645,
                   u'X':0.23009057343006134,
                   u'Type':u'leftEyeDown'
                },
                {  
                   u'Y':0.1452753245830536,
                   u'X':0.2710612118244171,
                   u'Type':u'rightEyeLeft'
                },
                {  
                   u'Y':0.14650410413742065,
                   u'X':0.290282666683197,
                   u'Type':u'rightEyeRight'
                },
                {  
                   u'Y':0.14003470540046692,
                   u'X':0.2805991768836975,
                   u'Type':u'rightEyeUp'
                },
                {  
                   u'Y':0.1502566933631897,
                   u'X':0.28069600462913513,
                   u'Type':u'rightEyeDown'
                },
                {  
                   u'Y':0.18839149177074432,
                   u'X':0.24658267199993134,
                   u'Type':u'noseLeft'
                },
                {  
                   u'Y':0.1907956302165985,
                   u'X':0.2669946551322937,
                   u'Type':u'noseRight'
                },
                {  
                   u'Y':0.20502744615077972,
                   u'X':0.2580716609954834,
                   u'Type':u'mouthUp'
                },
                {  
                   u'Y':0.2304033786058426,
                   u'X':0.25829872488975525,
                   u'Type':u'mouthDown'
                }
             ],
             u'Pose':{  
                u'Yaw':0.48987358808517456,
                u'Roll':5.123720645904541,
                u'Pitch':3.6710681915283203
             },
             u'Emotions':[  
                {  
                   u'Confidence':43.91263198852539,
                   u'Type':u'CALM'
                },
                {  
                   u'Confidence':9.353935241699219,
                   u'Type':u'SAD'
                },
                {  
                   u'Confidence':3.8915693759918213,
                   u'Type':u'SURPRISED'
                }
             ],
             u'AgeRange':{  
                u'High':45,
                u'Low':29
             },
             u'EyesOpen':{  
                u'Confidence':99.91922760009766,
                u'Value':True
             },
             u'BoundingBox':{  
                u'Width':0.15111111104488373,
                u'Top':0.0555555559694767,
                u'Left':0.18000000715255737,
                u'Height':0.20987653732299805
             },
             u'Smile':{  
                u'Confidence':95.19852447509766,
                u'Value':False
             },
             u'MouthOpen':{  
                u'Confidence':96.45076751708984,
                u'Value':False
             },
             u'Quality':{  
                u'Sharpness':99.9945297241211,
                u'Brightness':43.15739440917969
             },
             u'Mustache':{  
                u'Confidence':99.99900817871094,
                u'Value':True
             },
             u'Beard':{  
                u'Confidence':99.99919891357422,
                u'Value':True
             }
          },
          {  
             u'Confidence':99.99992370605469,
             u'Eyeglasses':{  
                u'Confidence':99.65634155273438,
                u'Value':False
             },
             u'Sunglasses':{  
                u'Confidence':99.96814727783203,
                u'Value':False
             },
             u'Gender':{  
                u'Confidence':100.0,
                u'Value':u'Female'
             },
             u'Landmarks':[  
                {  
                   u'Y':0.26706254482269287,
                   u'X':0.7707092761993408,
                   u'Type':u'eyeLeft'
                },
                {  
                   u'Y':0.26079681515693665,
                   u'X':0.814210832118988,
                   u'Type':u'eyeRight'
                },
                {  
                   u'Y':0.2996937036514282,
                   u'X':0.7927810549736023,
                   u'Type':u'nose'
                },
                {  
                   u'Y':0.3217785358428955,
                   u'X':0.7760947942733765,
                   u'Type':u'mouthLeft'
                },
                {  
                   u'Y':0.31633180379867554,
                   u'X':0.8113355040550232,
                   u'Type':u'mouthRight'
                },
                {  
                   u'Y':0.26539212465286255,
                   u'X':0.7726847529411316,
                   u'Type':u'leftPupil'
                },
                {  
                   u'Y':0.2598623037338257,
                   u'X':0.815914511680603,
                   u'Type':u'rightPupil'
                },
                {  
                   u'Y':0.25672996044158936,
                   u'X':0.7544487118721008,
                   u'Type':u'leftEyeBrowLeft'
                },
                {  
                   u'Y':0.2517096996307373,
                   u'X':0.7666251063346863,
                   u'Type':u'leftEyeBrowRight'
                },
                {  
                   u'Y':0.25500333309173584,
                   u'X':0.780444324016571,
                   u'Type':u'leftEyeBrowUp'
                },
                {  
                   u'Y':0.2507365345954895,
                   u'X':0.8030867576599121,
                   u'Type':u'rightEyeBrowLeft'
                },
                {  
                   u'Y':0.243417426943779,
                   u'X':0.8174728751182556,
                   u'Type':u'rightEyeBrowRight'
                },
                {  
                   u'Y':0.24672727286815643,
                   u'X':0.831135094165802,
                   u'Type':u'rightEyeBrowUp'
                },
                {  
                   u'Y':0.2684835195541382,
                   u'X':0.7621931433677673,
                   u'Type':u'leftEyeLeft'
                },
                {  
                   u'Y':0.26779988408088684,
                   u'X':0.7796010971069336,
                   u'Type':u'leftEyeRight'
                },
                {  
                   u'Y':0.2625950872898102,
                   u'X':0.7702999114990234,
                   u'Type':u'leftEyeUp'
                },
                {  
                   u'Y':0.2704508602619171,
                   u'X':0.7709307074546814,
                   u'Type':u'leftEyeDown'
                },
                {  
                   u'Y':0.2640814483165741,
                   u'X':0.8058761358261108,
                   u'Type':u'rightEyeLeft'
                },
                {  
                   u'Y':0.2597113251686096,
                   u'X':0.8229840993881226,
                   u'Type':u'rightEyeRight'
                },
                {  
                   u'Y':0.25640150904655457,
                   u'X':0.8134826421737671,
                   u'Type':u'rightEyeUp'
                },
                {  
                   u'Y':0.2640925347805023,
                   u'X':0.8147196173667908,
                   u'Type':u'rightEyeDown'
                },
                {  
                   u'Y':0.3055744171142578,
                   u'X':0.7856976389884949,
                   u'Type':u'noseLeft'
                },
                {  
                   u'Y':0.3036910593509674,
                   u'X':0.8011425733566284,
                   u'Type':u'noseRight'
                },
                {  
                   u'Y':0.31992536783218384,
                   u'X':0.7932916879653931,
                   u'Type':u'mouthUp'
                },
                {  
                   u'Y':0.33520761132240295,
                   u'X':0.79485684633255,
                   u'Type':u'mouthDown'
                }
             ],
             u'Pose':{  
                u'Yaw':-0.06331443041563034,
                u'Roll':-6.203024864196777,
                u'Pitch':-7.0949506759643555
             },
             u'Emotions':[  
                {  
                   u'Confidence':89.2152328491211,
                   u'Type':u'HAPPY'
                },
                {  
                   u'Confidence':9.729451179504395,
                   u'Type':u'CALM'
                },
                {  
                   u'Confidence':0.6038248538970947,
                   u'Type':u'SAD'
                }
             ],
             u'AgeRange':{  
                u'High':44,
                u'Low':27
             },
             u'EyesOpen':{  
                u'Confidence':99.99740600585938,
                u'Value':True
             },
             u'BoundingBox':{  
                u'Width':0.1088888868689537,
                u'Top':0.20061728358268738,
                u'Left':0.7388888597488403,
                u'Height':0.15123456716537476
             },
             u'Smile':{  
                u'Confidence':95.67159271240234,
                u'Value':True
             },
             u'MouthOpen':{  
                u'Confidence':94.17918395996094,
                u'Value':False
             },
             u'Quality':{  
                u'Sharpness':99.9945297241211,
                u'Brightness':39.26359558105469
             },
             u'Mustache':{  
                u'Confidence':99.99170684814453,
                u'Value':False
             },
             u'Beard':{  
                u'Confidence':99.99835205078125,
                u'Value':False
             }
          },
          {  
             u'Confidence':99.96034240722656,
             u'Eyeglasses':{  
                u'Confidence':99.92039489746094,
                u'Value':False
             },
             u'Sunglasses':{  
                u'Confidence':99.93636322021484,
                u'Value':False
             },
             u'Gender':{  
                u'Confidence':100.0,
                u'Value':u'Female'
             },
             u'Landmarks':[  
                {  
                   u'Y':0.18232567608356476,
                   u'X':0.5778844356536865,
                   u'Type':u'eyeLeft'
                },
                {  
                   u'Y':0.16774585843086243,
                   u'X':0.6128805875778198,
                   u'Type':u'eyeRight'
                },
                {  
                   u'Y':0.20837736129760742,
                   u'X':0.5959003567695618,
                   u'Type':u'nose'
                },
                {  
                   u'Y':0.22833490371704102,
                   u'X':0.5887420773506165,
                   u'Type':u'mouthLeft'
                },
                {  
                   u'Y':0.21769492328166962,
                   u'X':0.6171351671218872,
                   u'Type':u'mouthRight'
                },
                {  
                   u'Y':0.1805136352777481,
                   u'X':0.579119086265564,
                   u'Type':u'leftPupil'
                },
                {  
                   u'Y':0.1658496856689453,
                   u'X':0.6126954555511475,
                   u'Type':u'rightPupil'
                },
                {  
                   u'Y':0.16765351593494415,
                   u'X':0.5615187287330627,
                   u'Type':u'leftEyeBrowLeft'
                },
                {  
                   u'Y':0.16383837163448334,
                   u'X':0.572333574295044,
                   u'Type':u'leftEyeBrowRight'
                },
                {  
                   u'Y':0.16688108444213867,
                   u'X':0.5837448239326477,
                   u'Type':u'leftEyeBrowUp'
                },
                {  
                   u'Y':0.15993839502334595,
                   u'X':0.5987500548362732,
                   u'Type':u'rightEyeBrowLeft'
                },
                {  
                   u'Y':0.1463216096162796,
                   u'X':0.609968900680542,
                   u'Type':u'rightEyeBrowRight'
                },
                {  
                   u'Y':0.1443294882774353,
                   u'X':0.6236896514892578,
                   u'Type':u'rightEyeBrowUp'
                },
                {  
                   u'Y':0.18486005067825317,
                   u'X':0.570555567741394,
                   u'Type':u'leftEyeLeft'
                },
                {  
                   u'Y':0.18086780607700348,
                   u'X':0.5857896208763123,
                   u'Type':u'leftEyeRight'
                },
                {  
                   u'Y':0.17860934138298035,
                   u'X':0.5771691799163818,
                   u'Type':u'leftEyeUp'
                },
                {  
                   u'Y':0.1855037957429886,
                   u'X':0.5783115029335022,
                   u'Type':u'leftEyeDown'
                },
                {  
                   u'Y':0.17199330031871796,
                   u'X':0.6058240532875061,
                   u'Type':u'rightEyeLeft'
                },
                {  
                   u'Y':0.16506175696849823,
                   u'X':0.6202465891838074,
                   u'Type':u'rightEyeRight'
                },
                {  
                   u'Y':0.1641407310962677,
                   u'X':0.6118557453155518,
                   u'Type':u'rightEyeUp'
                },
                {  
                   u'Y':0.17056936025619507,
                   u'X':0.6137507557868958,
                   u'Type':u'rightEyeDown'
                },
                {  
                   u'Y':0.21560631692409515,
                   u'X':0.5929023623466492,
                   u'Type':u'noseLeft'
                },
                {  
                   u'Y':0.20934517681598663,
                   u'X':0.6062437891960144,
                   u'Type':u'noseRight'
                },
                {  
                   u'Y':0.22505661845207214,
                   u'X':0.6027432680130005,
                   u'Type':u'mouthUp'
                },
                {  
                   u'Y':0.23373855650424957,
                   u'X':0.6051225066184998,
                   u'Type':u'mouthDown'
                }
             ],
             u'Pose':{  
                u'Yaw':-11.456254005432129,
                u'Roll':-16.89837074279785,
                u'Pitch':-13.658872604370117
             },
             u'Emotions':[  
                {  
                   u'Confidence':99.14630889892578,
                   u'Type':u'HAPPY'
                },
                {  
                   u'Confidence':1.8018364906311035,
                   u'Type':u'SAD'
                },
                {  
                   u'Confidence':0.9208798408508301,
                   u'Type':u'CALM'
                }
             ],
             u'AgeRange':{  
                u'High':45,
                u'Low':29
             },
             u'EyesOpen':{  
                u'Confidence':99.99982452392578,
                u'Value':True
             },
             u'BoundingBox':{  
                u'Width':0.10444444417953491,
                u'Top':0.1111111119389534,
                u'Left':0.54666668176651,
                u'Height':0.14506173133850098
             },
             u'Smile':{  
                u'Confidence':98.27970123291016,
                u'Value':True
             },
             u'MouthOpen':{  
                u'Confidence':99.52448272705078,
                u'Value':False
             },
             u'Quality':{  
                u'Sharpness':99.99090576171875,
                u'Brightness':55.04219055175781
             },
             u'Mustache':{  
                u'Confidence':99.85346221923828,
                u'Value':False
             },
             u'Beard':{  
                u'Confidence':99.89535522460938,
                u'Value':False
             }
          },
          {  
             u'Confidence':99.99982452392578,
             u'Eyeglasses':{  
                u'Confidence':99.99952697753906,
                u'Value':False
             },
             u'Sunglasses':{  
                u'Confidence':99.85890197753906,
                u'Value':False
             },
             u'Gender':{  
                u'Confidence':100.0,
                u'Value':u'Female'
             },
             u'Landmarks':[  
                {  
                   u'Y':0.22449246048927307,
                   u'X':0.4206644892692566,
                   u'Type':u'eyeLeft'
                },
                {  
                   u'Y':0.21921640634536743,
                   u'X':0.45507532358169556,
                   u'Type':u'eyeRight'
                },
                {  
                   u'Y':0.25018519163131714,
                   u'X':0.4454347789287567,
                   u'Type':u'nose'
                },
                {  
                   u'Y':0.27047938108444214,
                   u'X':0.4255673885345459,
                   u'Type':u'mouthLeft'
                },
                {  
                   u'Y':0.2645663619041443,
                   u'X':0.4581734538078308,
                   u'Type':u'mouthRight'
                },
                {  
                   u'Y':0.22426381707191467,
                   u'X':0.42381539940834045,
                   u'Type':u'leftPupil'
                },
                {  
                   u'Y':0.2180921733379364,
                   u'X':0.4551822245121002,
                   u'Type':u'rightPupil'
                },
                {  
                   u'Y':0.21364419162273407,
                   u'X':0.4079684019088745,
                   u'Type':u'leftEyeBrowLeft'
                },
                {  
                   u'Y':0.2071036845445633,
                   u'X':0.41601595282554626,
                   u'Type':u'leftEyeBrowRight'
                },
                {  
                   u'Y':0.20785531401634216,
                   u'X':0.4259326159954071,
                   u'Type':u'leftEyeBrowUp'
                },
                {  
                   u'Y':0.2037205696105957,
                   u'X':0.4488908350467682,
                   u'Type':u'rightEyeBrowLeft'
                },
                {  
                   u'Y':0.19996026158332825,
                   u'X':0.45777177810668945,
                   u'Type':u'rightEyeBrowRight'
                },
                {  
                   u'Y':0.203616201877594,
                   u'X':0.4662401080131531,
                   u'Type':u'rightEyeBrowUp'
                },
                {  
                   u'Y':0.22690433263778687,
                   u'X':0.4141393005847931,
                   u'Type':u'leftEyeLeft'
                },
                {  
                   u'Y':0.2247251570224762,
                   u'X':0.42744001746177673,
                   u'Type':u'leftEyeRight'
                },
                {  
                   u'Y':0.22096996009349823,
                   u'X':0.42041951417922974,
                   u'Type':u'leftEyeUp'
                },
                {  
                   u'Y':0.22669261693954468,
                   u'X':0.42078423500061035,
                   u'Type':u'leftEyeDown'
                },
                {  
                   u'Y':0.22186797857284546,
                   u'X':0.4480724334716797,
                   u'Type':u'rightEyeLeft'
                },
                {  
                   u'Y':0.21955153346061707,
                   u'X':0.46198514103889465,
                   u'Type':u'rightEyeRight'
                },
                {  
                   u'Y':0.21536925435066223,
                   u'X':0.4547673165798187,
                   u'Type':u'rightEyeUp'
                },
                {  
                   u'Y':0.22157010436058044,
                   u'X':0.4554298222064972,
                   u'Type':u'rightEyeDown'
                },
                {  
                   u'Y':0.25525006651878357,
                   u'X':0.4360193908214569,
                   u'Type':u'noseLeft'
                },
                {  
                   u'Y':0.25191637873649597,
                   u'X':0.45096325874328613,
                   u'Type':u'noseRight'
                },
                {  
                   u'Y':0.26558181643486023,
                   u'X':0.4436923563480377,
                   u'Type':u'mouthUp'
                },
                {  
                   u'Y':0.2819337248802185,
                   u'X':0.4448675215244293,
                   u'Type':u'mouthDown'
                }
             ],
             u'Pose':{  
                u'Yaw':13.742110252380371,
                u'Roll':-7.460667133331299,
                u'Pitch':-4.507489204406738
             },
             u'Emotions':[  
                {  
                   u'Confidence':97.51264190673828,
                   u'Type':u'HAPPY'
                },
                {  
                   u'Confidence':1.9313514232635498,
                   u'Type':u'CALM'
                },
                {  
                   u'Confidence':0.7164835929870605,
                   u'Type':u'SAD'
                }
             ],
             u'AgeRange':{  
                u'High':52,
                u'Low':35
             },
             u'EyesOpen':{  
                u'Confidence':99.9980239868164,
                u'Value':True
             },
             u'BoundingBox':{  
                u'Width':0.10111111402511597,
                u'Top':0.16512346267700195,
                u'Left':0.38777777552604675,
                u'Height':0.14043210446834564
             },
             u'Smile':{  
                u'Confidence':90.77119445800781,
                u'Value':True
             },
             u'MouthOpen':{  
                u'Confidence':83.23787689208984,
                u'Value':False
             },
             u'Quality':{  
                u'Sharpness':99.99090576171875,
                u'Brightness':45.460960388183594
             },
             u'Mustache':{  
                u'Confidence':98.86227416992188,
                u'Value':False
             },
             u'Beard':{  
                u'Confidence':98.3800048828125,
                u'Value':False
             }
          },
          {  
             u'Confidence':99.98088836669922,
             u'Eyeglasses':{  
                u'Confidence':99.9983901977539,
                u'Value':False
             },
             u'Sunglasses':{  
                u'Confidence':99.13247680664062,
                u'Value':False
             },
             u'Gender':{  
                u'Confidence':100.0,
                u'Value':u'Female'
             },
             u'Landmarks':[  
                {  
                   u'Y':0.2737465500831604,
                   u'X':0.9162755608558655,
                   u'Type':u'eyeLeft'
                },
                {  
                   u'Y':0.2731752097606659,
                   u'X':0.9395505785942078,
                   u'Type':u'eyeRight'
                },
                {  
                   u'Y':0.2968725264072418,
                   u'X':0.9235119223594666,
                   u'Type':u'nose'
                },
                {  
                   u'Y':0.3034268021583557,
                   u'X':0.9212521314620972,
                   u'Type':u'mouthLeft'
                },
                {  
                   u'Y':0.30086851119995117,
                   u'X':0.9415357112884521,
                   u'Type':u'mouthRight'
                },
                {  
                   u'Y':0.2743266224861145,
                   u'X':0.9167730808258057,
                   u'Type':u'leftPupil'
                },
                {  
                   u'Y':0.27314165234565735,
                   u'X':0.9400665163993835,
                   u'Type':u'rightPupil'
                },
                {  
                   u'Y':0.26544690132141113,
                   u'X':0.9083455801010132,
                   u'Type':u'leftEyeBrowLeft'
                },
                {  
                   u'Y':0.2658803462982178,
                   u'X':0.913865327835083,
                   u'Type':u'leftEyeBrowRight'
                },
                {  
                   u'Y':0.2673903703689575,
                   u'X':0.9187251329421997,
                   u'Type':u'leftEyeBrowUp'
                },
                {  
                   u'Y':0.26711151003837585,
                   u'X':0.9312921166419983,
                   u'Type':u'rightEyeBrowLeft'
                },
                {  
                   u'Y':0.26339757442474365,
                   u'X':0.9393160939216614,
                   u'Type':u'rightEyeBrowRight'
                },
                {  
                   u'Y':0.2638857364654541,
                   u'X':0.9474143981933594,
                   u'Type':u'rightEyeBrowUp'
                },
                {  
                   u'Y':0.2736878991127014,
                   u'X':0.911957859992981,
                   u'Type':u'leftEyeLeft'
                },
                {  
                   u'Y':0.27365249395370483,
                   u'X':0.9207517504692078,
                   u'Type':u'leftEyeRight'
                },
                {  
                   u'Y':0.27223506569862366,
                   u'X':0.9162012934684753,
                   u'Type':u'leftEyeUp'
                },
                {  
                   u'Y':0.27533426880836487,
                   u'X':0.9162706136703491,
                   u'Type':u'leftEyeDown'
                },
                {  
                   u'Y':0.2737123370170593,
                   u'X':0.9349683523178101,
                   u'Type':u'rightEyeLeft'
                },
                {  
                   u'Y':0.2726210951805115,
                   u'X':0.9440947771072388,
                   u'Type':u'rightEyeRight'
                },
                {  
                   u'Y':0.27148813009262085,
                   u'X':0.9394481182098389,
                   u'Type':u'rightEyeUp'
                },
                {  
                   u'Y':0.2748708426952362,
                   u'X':0.93967205286026,
                   u'Type':u'rightEyeDown'
                },
                {  
                   u'Y':0.29760974645614624,
                   u'X':0.9215348362922668,
                   u'Type':u'noseLeft'
                },
                {  
                   u'Y':0.2963670790195465,
                   u'X':0.9320175647735596,
                   u'Type':u'noseRight'
                },
                {  
                   u'Y':0.3021548092365265,
                   u'X':0.9292097687721252,
                   u'Type':u'mouthUp'
                },
                {  
                   u'Y':0.3129018247127533,
                   u'X':0.9302055239677429,
                   u'Type':u'mouthDown'
                }
             ],
             u'Pose':{  
                u'Yaw':-26.629114151000977,
                u'Roll':0.0670856237411499,
                u'Pitch':-22.471994400024414
             },
             u'Emotions':[  
                {  
                   u'Confidence':97.27491760253906,
                   u'Type':u'HAPPY'
                },
                {  
                   u'Confidence':2.9502570629119873,
                   u'Type':u'SURPRISED'
                },
                {  
                   u'Confidence':1.9262492656707764,
                   u'Type':u'DISGUSTED'
                }
             ],
             u'AgeRange':{  
                u'High':43,
                u'Low':26
             },
             u'EyesOpen':{  
                u'Confidence':67.57186889648438,
                u'Value':True
             },
             u'BoundingBox':{  
                u'Width':0.06333333253860474,
                u'Top':0.23456789553165436,
                u'Left':0.897777795791626,
                u'Height':0.08796296268701553
             },
             u'Smile':{  
                u'Confidence':74.0545425415039,
                u'Value':True
             },
             u'MouthOpen':{  
                u'Confidence':62.88851547241211,
                u'Value':False
             },
             u'Quality':{  
                u'Sharpness':99.1240463256836,
                u'Brightness':33.562618255615234
             },
             u'Mustache':{  
                u'Confidence':99.92550659179688,
                u'Value':False
             },
             u'Beard':{  
                u'Confidence':99.9753189086914,
                u'Value':False
             }
          }
       ],
       'ResponseMetadata':{  
          'RetryAttempts':0,
          'HTTPStatusCode':200,
          'RequestId':'06360ca0-551c-11e7-84ae-b99628b0dd2b',
          'HTTPHeaders':{  
             'date':'Mon, 19 Jun 2017 18:20:59 GMT',
             'x-amzn-requestid':'06360ca0-551c-11e7-84ae-b99628b0dd2b',
             'content-length':'13601',
             'content-type':'application/x-amz-json-1.1',
             'connection':'keep-alive'
          }
       },
       u'OrientationCorrection':u'ROTATE_0'
    }
    
    '''

    def detect_face(self, raw_img):
        print('detecting faces')
        face = self.rekognition_client.detect_faces(
            Image={
                'Bytes': raw_img,
            },
            Attributes=[
                'ALL',
            ]
        )

        if not face['FaceDetails']:
            print('no face detected')
        else:
            print('there is ' + repr(len(face['FaceDetails'])) + ' faces')
            im = Image.open(io.BytesIO(raw_img))
            for face in face['FaceDetails']:
                im = ImageUtils.draw_box(face['BoundingBox']['Top'], face['BoundingBox']['Left'],
                                         face['BoundingBox']['Width'], face['BoundingBox']['Height'], im)
            im.save("toto.png", "PNG")

        return face

    '''{
       'ResponseMetadata':{
          'RetryAttempts':0,
          'HTTPStatusCode':200,
          'RequestId':'4b0a3ede-3e39-11e7-8965-6b1eadbb90cb',
          'HTTPHeaders':{
             'date':'Sun, 21 May 2017 15:22:37 GMT',
             'x-amzn-requestid':'4b0a3ede-3e39-11e7-8965-6b1eadbb90cb',
             'content-length':'6889',
             'content-type':'application/x-amz-json-1.1',
             'connection':'keep-alive'
          }
       },
       u'FaceMatches':[
          {
             u'Face':{
                u'BoundingBox':{
                   u'Width':0.18444444239139557,
                   u'Top':0.3893280625343323,
                   u'Left':0.30000001192092896,
                   u'Height':0.32608696818351746
                },
                u'Confidence':99.9843521118164
             },
             u'Similarity':88.0
          }
       ],
       u'SourceImageFace':{
          u'BoundingBox':{
             u'Width':0.6503496766090393,
             u'Top':0.22610722482204437,
             u'Left':0.20279720425605774,
             u'Height':0.4335664212703705
          },
          u'Confidence':99.95665740966797
       }
    }'''

    def compare_faces(self, raw_image_ref, raw_image_to_analyze):
        print("doing facial recognition")
        faces = self.rekognition_client.compare_faces(
            SourceImage={
                'Bytes': raw_image_ref,
            },
            TargetImage={
                'Bytes': raw_image_to_analyze
            },
            SimilarityThreshold=80
        )

        if not faces['FaceMatches']:
            print("no faces matched")
        else:
            im = Image.open(io.BytesIO(raw_image_to_analyze))
            for face in faces['FaceMatches']:
                ImageUtils.draw_box(face['Face']['BoundingBox']['Top'], face['Face']['BoundingBox']['Left'],
                                    face['Face']['BoundingBox']['Width'], face['Face']['BoundingBox']['Height'], im)
            im.save("toto.png", "PNG")

        return faces
