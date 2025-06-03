export default function FilterSection() {
  return (
    <div>
        <p className="text-lg mb-4 mt-2 font-bold">Filters</p>
        <div className="flex flex-row gap-x-2">
            <input type="checkbox"/><p>Computer Science & Engineering</p>
        </div>
        <div className="flex flex-row gap-x-2">
            <input type="checkbox"/><p>Business</p>
        </div>
        <div className="flex flex-row gap-x-2">
            <input type="checkbox"/><p>Mathetmatics</p>
        </div>
        <div className="flex flex-row gap-x-2">
            <input type="checkbox"/><p>Physics</p>
        </div>
    </div>
  )
}
