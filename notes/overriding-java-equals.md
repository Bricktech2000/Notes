# Overriding Java Equals

see [[polymorphism]], [[java-is-a-terrible-language]]

overriding the `Object.equals` in Java must follow the pattern below &mdash; [[iti1121-c-introduction-to-computing-ii]]

```java
public class Account {
	private int id;
	private String name;
	// ...
	public boolean equals(Object o) {
		if (o == null) return false;
		if (getClass() != o.getClass()) return false;
		// if (!(o instanceof Account)) return false; // alternative

		Account other = (Account) o;
		if (id != other.id) return false;
		if (name == null && other.name != null) return false;
		if (name != null && !name.equals(other.name)) return false;

		return true;
  }
}
```
