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
      @name = @user.name
      @user.name
    last_name_property: ->
      @last_name = @user.last_name
      @user.last_name
    birthday_property: ->
      @birthday = @user.birthday
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
    setUpDateTimePicker: ->
      if not @read_mode
        $('.datetime').bootstrapMaterialDatePicker(
          date: true
          time: false
        ).on
          change: =>
            @birthday = $('.datetime').val()
            @update()