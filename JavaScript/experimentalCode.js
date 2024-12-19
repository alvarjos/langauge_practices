// saveQuery code for dataSource.controllers
const saveQuery = async (req, res, next) => {
  const { params, body: query, dataSources } = req

  if (params.queryId !== query.id) {
    return void next(new NotFoundError(`Query index record for id ${params.queryId} does not exist`))
  }

  const queryId = await dataSources.content.saveCurrentActive(req.body)

  req.responseData = {
    ...req.responseData,
    ...queryId
  }

  const { result } = queryId

  const status = {
    updated: 200,
    created: 201
  }

  res.status(status[result])

  next()
}