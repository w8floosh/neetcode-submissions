// Checks inclusion of permuted s1 in s2, therefore len(s2) > len(s1)
func checkInclusion(s1 string, s2 string) bool {
	if len(s2) < len(s1) {
		return false
	}

	for i := 0; i <= len(s2)-len(s1); i++ {
		if isPermutation(s1, s2[i:i+len(s1)]) {
			return true
		}
	}

	return false
}

// Uses a rolling polynomial hash
func isPermutation(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	var hash1, hash2, base, mod uint64
	base = 97 // prime number
	mod = 1e9 + 7 // to avoid hash numbers explosion

	for i := 0; i < len(s1); i++ {
		hash1 = (hash1 + powInt(base, uint64(s1[i]))) % mod
		hash2 = (hash2 + powInt(base, uint64(s2[i]))) % mod
	}

	return hash1 == hash2
}

func powInt(base, exp uint64) uint64 {
    result := uint64(1)
    for exp > 0 {
        if exp & 1 == 1 {
            result = (result * base) % 1000000007
        }
        base = (base * base) % 1000000007
        exp >>= 1
    }
    return result
}