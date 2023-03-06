{
	"info": {
		"_postman_id": "6ba2b335-11de-4125-892a-92fdb3c55fe9",
		"name": "Fandit",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "25683238"
	},
	"item": [
		{
			"name": "Zoo/ los endpoints de esta lista no esta terminados",
			"item": [
				{
					"name": "Obtener listado de zoologicos",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/zoo/api",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zoo",
								"api"
							]
						}
					},
					"response": []
				},
				{
					"name": "registrar un zoologico",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "Bilbao Zoo",
									"type": "text"
								},
								{
									"key": "city",
									"value": "Bilbao",
									"type": "text"
								},
								{
									"key": "country",
									"value": "Spain",
									"type": "text"
								},
								{
									"key": "surface",
									"value": "10000",
									"type": "text"
								},
								{
									"key": "budget",
									"value": "1000000",
									"type": "text"
								},
								{
									"key": "animals",
									"value": "Procyon",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/zoo/api",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zoo",
								"api"
							]
						}
					},
					"response": []
				},
				{
					"name": "Modificar un registro",
					"request": {
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "Bilbao Zoo",
									"type": "text"
								},
								{
									"key": "city",
									"value": "Bilbao",
									"type": "text"
								},
								{
									"key": "country",
									"value": "Spain",
									"type": "text"
								},
								{
									"key": "surface",
									"value": "10000",
									"type": "text"
								},
								{
									"key": "budget",
									"value": "1000000",
									"type": "text"
								},
								{
									"key": "animals",
									"value": "Procyon",
									"type": "text",
									"disabled": true
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/zoo/api/8/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zoo",
								"api",
								"8",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "New Request",
					"request": {
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/zoo/api/10/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zoo",
								"api",
								"10",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "zooViewSet",
			"item": [
				{
					"name": "Get",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/zooViewSets/zoo/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zooViewSets",
								"zoo",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Post",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "",
								"value": "",
								"type": "text",
								"disabled": true
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "Valencia spa Zoo",
									"type": "text"
								},
								{
									"key": "city",
									"value": "Valencia",
									"type": "text"
								},
								{
									"key": "country",
									"value": "Spain",
									"type": "text"
								},
								{
									"key": "surface",
									"value": "50000",
									"type": "text"
								},
								{
									"key": "budget",
									"value": "20000000",
									"type": "text"
								},
								{
									"key": "animals",
									"type": "file",
									"src": []
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/zooViewSets/zoo/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zooViewSets",
								"zoo",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Put",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "",
								"value": "",
								"type": "text",
								"disabled": true
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "Valencia spa Zoo",
									"type": "text"
								},
								{
									"key": "city",
									"value": "Valencia",
									"type": "text"
								},
								{
									"key": "country",
									"value": "Spain",
									"type": "text"
								},
								{
									"key": "surface",
									"value": "50000",
									"type": "text"
								},
								{
									"key": "budget",
									"value": "20000000",
									"type": "text"
								},
								{
									"key": "animals",
									"type": "file",
									"src": []
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/zooViewSets/zoo/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zooViewSets",
								"zoo",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/zooViewSets/zoo/9/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"zooViewSets",
								"zoo",
								"9",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Animal",
			"item": [
				{
					"name": "Get",
					"request": {
						"method": "GET",
						"header": []
					},
					"response": []
				},
				{
					"name": "Post",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "common_name",
									"value": "ardilla",
									"type": "text"
								},
								{
									"key": "scientific_name",
									"value": "ardilla",
									"type": "text"
								},
								{
									"key": "family_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "in_extintion",
									"value": "false",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/animal/animal/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"animal",
								"animal",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Put",
					"request": {
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "common_name",
									"value": "ardilla",
									"type": "text"
								},
								{
									"key": "scientific_name",
									"value": "ardilla",
									"type": "text"
								},
								{
									"key": "family_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "in_extintion",
									"value": "true",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/animal/animal/8/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"animal",
								"animal",
								"8",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "delete",
					"request": {
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/animal/animal/8/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"animal",
								"animal",
								"8",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Family",
			"item": [
				{
					"name": "Get",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/family/family/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"family",
								"family",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Post",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "marsupiales",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/family/family/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"family",
								"family",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Post Copy",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "marsupiales",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/family/family/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"family",
								"family",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "Post Copy 2",
					"request": {
						"method": "DELETE",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "marsupiales",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/family/family/8/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"family",
								"family",
								"8",
								""
							]
						}
					},
					"response": []
				}
			]
		}
	]
}