const axios = require('axios')

export function getGame (session) {
  return axios.get(`https://3f3d33749f7e.ngrok.io/api/game`,
    {
      headers: {
        session: session
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function newGame (session, id) {
  return axios.post(`https://3f3d33749f7e.ngrok.io/api/game`,
    JSON.stringify( {"id_person": id} ),
    {
      headers: {
        session: session,
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function sendAnswer (session, ans) {
  return axios.post(`https://3f3d33749f7e.ngrok.io/api/game/question`,
    JSON.stringify( {answer: ans} ),
    {
      headers: {
        session: session,
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function resumeGame (session) {
  return axios.get(`https://3f3d33749f7e.ngrok.io/api/game`,
    {
      headers: {
        session: session,
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}