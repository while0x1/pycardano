BLOCK_FROST_PROJECT_ID = <your_id>

chain_context = BlockFrostChainContext(project_id=BLOCK_FROST_PROJECT_ID,base_url=ApiUrls.preprod.value,)

address = <your_address>


utxos = chain_context.utxos(str(address))

assetDict = []
for utxo in utxos:
	if utxo.output.amount.multi_asset:
		assetDict.append(utxo.output.amount.multi_asset)

policies = []
for n in assetDict:
	for q in n:
		policies.append(q.to_primitive().hex())
    
    
