@ProfileController =
  extends: BaseController
  data: ->
    user: null
  components:
    'profile_photo': ProfilePhotoController
    'profile_info': ProfileInfoController
    'profile_address': ProfileAddressController
  created: ->
    User.me().then (user) =>
      @user = user[0]

new Vue(ProfileController).$mount '.container'
