@ProfileInfoController =
  extends: BaseController
  template: '#profile_info_tmpl'
  data: ->
    read_mode: true
    name: ''
    last_name: ''
    birthday: null
    verified: false
  computed:
    name_property: ->
      @user.name
    last_name_property: ->
      @user.last_name
    birthday_property: ->
      @user.birthday
    verified_property: ->
      @verified
  props: [
    'user'
  ]
  methods:
    edit: ->
      @read_mode = !@read_mode
    update: ->
      User.update(@user.id, @name, @last_name, @birthday, @verified)
