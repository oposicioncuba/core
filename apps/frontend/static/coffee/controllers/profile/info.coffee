@ProfileInfoController =
  extends: BaseController
  template: '#profile_info_tmpl'
  data: ->
    name: null
    last_name: null
    birthday: null
    verified: true
