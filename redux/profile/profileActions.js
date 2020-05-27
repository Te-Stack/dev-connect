import {
  getProfile,
  editProfileAPI,
  getUserProfileAPI,
} from "../../api/profileApi"
import * as types from "./profileTypes"
import Router from "next/router"
import {
  apiCallError,
  beginApiCall,
  apiCallSuccess,
} from "../apiStatus/apiActions"

export function loadProfileStart() {
  return { type: types.LOAD_PROFILE_START }
}

export function loadProfileSuccess(profiles) {
  return { type: types.LOAD_PROFILES, payload: profiles }
}

export function editProfileSuccess(profile) {
  return { type: types.EDIT_PROFILE, payload: profile }
}

export function loadUserProfileSucccess(profile) {
  return { type: types.GET_USER_PROFILE, payload: profile }
}

export function loadProfiles() {
  return function (dispatch) {
    dispatch(beginApiCall())
    dispatch(loadProfileStart())
    return getProfile()
      .then((profiles) => {
        dispatch(loadProfileSuccess(profiles.data))
        dispatch(apiCallSuccess())
      })
      .catch((error) => {
        dispatch(apiCallError(error))
      })
  }
}

export function loadUserProfile() {
  return function (dispatch) {
    dispatch(beginApiCall())

    dispatch(loadProfileStart())
    return getUserProfileAPI()
      .then((profile) => {
        dispatch(loadUserProfileSucccess(profile.data))
        dispatch(apiCallSuccess())
      })
      .catch((error) => {
        dispatch(apiCallError(error))
      })
  }
}

export function editProfileDispatch(values) {
  return function (dispatch) {
    dispatch(beginApiCall())

    return editProfileAPI(values)
      .then((profile) => {
        dispatch(editProfileSuccess(profile.data))
        dispatch(apiCallSuccess())
        Router.push("/dashboard")
      })
      .catch((error) => {
        console.log(error)

        dispatch(apiCallError(error))
      })
  }
}