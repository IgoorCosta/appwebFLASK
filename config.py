# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '5b0b8fe0-26e0-4b1d-b2ff-13c60f179452'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = 'e1e2ef26-b9f6-4258-9181-90e9774fe766'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '9cea78da-da99-4645-b501-fffc0201bb57'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '8b47ef95-fbab-4575-9d96-943b665e46dd'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '4iO8Q~xcrsF~1Nbq0gf4DPokEevrpR2tBrmEBa~p'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''