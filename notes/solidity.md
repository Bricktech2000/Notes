# Solidity

&mdash; <https://youtu.be/EhPeHeoKF88>

&mdash; <https://www.bitdegree.org/learn/solidity-variables>

[[solidity]] is an [[object-oriented programming]] language for implementing smart contracts on various [[blockchain]] platforms. also see [[cryptocurrency]]

[[class]] members (which represent state) are stored directly on the [[blockchain]] in [[solidity]]. the [[class]] `constructor` (which initializes state) is called exactly one time when the smart contract gets deployed to the [[blockchain]]

## data types

**see** [[type]]

```solidity
bool // boolean
int8..int256 // signed integers
uint8..uint256 // unsigned integers
bytes1..bytes32 // fixed-size byte array
address // 20-byte address
string // dynamic-size string
mapping // key-value store
struct, enum // user-defined types
```

> **note** `uint` and `int` are shorthands for `uint256` and `int256` respectively

> **example** _basic data types_
>
> ```solidity
> bool isReady = true;
> uint8 a = 1;
> int b = -1;
> address c = 0x1234567890123456789012345678901234567890;
> bytes32 d = "0x1234567890123456789012345678901234567890123456789012345678901234";
> string e = "hello world";
> ```

> **example** _[[abstract data type]]s_
>
> ```solidity
> uint[][] a = [[1, 2], [3, 4]];
> int[] b = new uint[](7);
>
> mapping(address => uint) balances = [0x1234567890123456789012345678901234567890 => 100];
> balances[0x1234567890123456789012345678901234567890] = 200;
> mapping(address => mapping(address => uint)) allowed;
> ```

> **example** _algebraic data [[type]]s_
>
> ```solidity
> struct Person {
>   string name;
>   uint age;
> }
>
> // ...
>
> Person p = Person("Alice", 20);
>
> ```

## modifiers and visibility

&mdash; <https://hashnode.com/post/pure-vs-view-in-solidity-cl04tbzlh07kaudnv1ial1gio>

```solidity
payable // can receive ether
constant // is computed at compile time
view // can read but not modify state
pure // cannot read nor modify state
public // can be called internally, externally, and by derived contracts. getters are automatically generated
private // can only be called internally. data marked private is still visible on the blockchain
external // can only be called externally
internal // can only be called internally and by derived contracts

returns (type) // returns a value of type `type`

modifier // user-defined modifiers
```

> **example** _user-defined modifiers_
>
> ```solidity
> modifier onlyOwner {
>   require(msg.sender == owner);
>   _;
> }
>
> modifier costs(uint price) {
>   require(msg.value >= price);
>   _;
> }
>
> function withdraw() public payable onlyOwner costs(2 ether) {
>   // ...
> }
> ```

## inheritance

```solidity
is, super
```

> **example** _[[inheritance]]_
>
> ```solidity
> contract A is Ownable {
>   constructor() public {
>     super;
>     // ...
>   }
>   // ...
> }
>
> ```

## factories

```solidity
new
```

> **example** _factory_
>
> ```solidity
> contract Contract {
>   uint public x;
>   // ...
> }
>
> contract Factory {
>   address public lastContract;
>
>   function create() public returns (address) {
>     lastContract = new Contract();
>     return lastContract;
>   }
>
>   function getLastContractX() public view returns (uint) {
>     return Contract(lastContract).x();
>   }
> }
>
> ```

## globals

```solidity
msg.sender // address of the sender
msg.value // amount of ether sent
block.timestamp // current block timestamp
block.number // current block number
block.difficulty // current block difficulty
// ...

require(condition, message) // throws `message` if `condition` is `false`
address(contract) // address of `contract`
```

> **example** _globals_
>
> ```solidity
> function get() public view returns (address) {
>   return address(this);
> }
>
> ```

## units

**see** [[international system of units]]

```solidity
wei // smallest unit of ether
szabo // 1 szabo == 10 ** 12 wei
finney // 1 finney == 10 ** 15 wei
ether // 1 ether == 10 ** 18 wei

seconds // one second
minutes // 1 minute == 60 seconds
hours // 1 hour == 60 minutes
days // 1 day == 24 hours
weeks // 1 week == 7 days
years // deprecated due to leap years
```

> **example**
>
> ```solidity
> return 1 ether;
> ```

## hello world

```solidity
pragma solidity ^0.8.0;

contract Counter {
  uint public count = 0;

  function increment() public {
    count += 1;
  }
}

```

## left to learn

```solidity
memory
bytes32..
pure
veiw
```
