@ProfileController =
  extends: BaseController
  data: ->
    user: null
  computed:
    photo: ->
      @user.photo
  components:
    'profile_photo': ProfilePhotoController
    'profile_info': ProfileInfoController
    'profile_address': ProfileAddressController
    'profile_organizations': ProfileOrganizationsController
  created: ->
    @loadUser()

  methods:
    loadUser: ->
      console.log 3333

      User.me().then (user) =>
        @user = user[0]

new Vue(ProfileController).$mount '.container'
