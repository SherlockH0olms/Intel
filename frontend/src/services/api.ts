import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Machines API
export const getMachines = () => api.get('/api/v1/machines')
export const getMachine = (id: string) => api.get(`/api/v1/machines/${id}`)
export const createMachine = (data: any) => api.post('/api/v1/machines', data)

// Sensors API
export const getSensorData = (machineId: string, params?: any) => 
  api.get(`/api/v1/sensors/${machineId}`, { params })

// Recommendations API
export const getRecommendations = (machineId: string) => 
  api.get(`/api/v1/recommendations/${machineId}`)

export const approveRecommendation = (id: string, data: any) => 
  api.post(`/api/v1/recommendations/${id}/approve`, data)

// Analytics API
export const getMetrics = (machineId?: string) => 
  api.get('/api/v1/analytics/metrics', { params: { machine_id: machineId } })

export const getTimeline = (days: number = 7) => 
  api.get('/api/v1/analytics/timeline', { params: { days } })

// Defects API
export const detectDefects = (file: File, machineId: string) => {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('machine_id', machineId)
  return api.post('/api/v1/defects/detect', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
}

export default api