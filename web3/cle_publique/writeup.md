```
function isPublicKey(bytes memory mystery) external view returns(bool){
        require(address(uint160(uint256(keccak256(mystery)))) == secretAddress, "Essayez encore !")}
```
Addr : `0xd22213f7B4E5997C9B542105cce6ed4dfEAE5F91`

Pas de mystère, il va falloir trouver un mystery tel qu'il soit égal à l'adresse

Fonctions :
uint160, uint256, keccak256, address

Inputs :
bytes memory

