const axios = require('axios')

export function registerUser(data) {
    return axios.post(`http://192.168.0.117/api/user/register`, JSON.stringify(data),
        {
            headers: {
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

export function authUser(data) {
    return axios.post(`http://192.168.0.117/api/user/login`, JSON.stringify(data),
        {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function (response) {
            console.log(response.data)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getPerson() {
    return axios.get(`http://192.168.0.117/api/person`)
        .then(function (response) {
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getRating() {
    return axios.get(`http://192.168.0.117/api/rating`,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getProfile() {
    return axios.get(`http://192.168.0.117/api/user/profile`,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getProfileInfo(id_user) {
    return axios.get(`http://192.168.0.117/api/user/` + id_user,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}
