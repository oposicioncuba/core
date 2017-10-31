@ProfileController =
  extends: BaseController
  components:
    'profile_photo': ProfilePhotoController
    'profile_info': ProfileInfoController
    'profile_address': ProfileAddressController

new Vue(ProfileController).$mount '.container'
