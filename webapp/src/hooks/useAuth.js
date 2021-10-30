import axios from 'axios'

const AUTH_URL = process.env.REACT_APP_BASEURL + 'auth-token/'
const API_URL = process.env.REACT_APP_API_ENDPOIN

async function auth (data, setHttpError, addUser, addAuthToken) {
  await axios.post(
    AUTH_URL, {
      username: data.username,
      password: data.password
    }
  ).then(response => {
    const token = response.data.token
    addAuthToken(token)
    window.localStorage.setItem('auth_token', token)
    getMe(token).then((response) => {
      window.sessionStorage.setItem('user', JSON.stringify(response.data))
      addUser(response.data)
    })
  }
  ).catch(err => {
    const error = {}

    if (err.response) {
      error.non_field_errors = err.response.data.non_field_errors
      error.status = err.response.status
      error.headers = err.response.headers
    }
    if (err.message) {
      error.message = err.message
    }
    setHttpError(error)
  })
}

async function getMe (token) {
  const config = {
    method: 'get',
    url: API_URL + 'users/me/',
    headers: {
      Authorization: 'Token ' + token
    }
  }
  return axios(config)
}

export { auth }
