@ProfileController =
  extends: BaseController
  data: ->
    user: null
  components:
    'profile_photo': ProfilePhotoController
    'profile_info': ProfileInfoController
    'profile_address': ProfileAddressController
  methods:
    initialize: ->
      @user = User.me()

new Vue(ProfileController).$mount '.container'
