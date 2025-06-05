export default function FilterSection() {
  return (
    <div>
      <p className="text-lg mt-2 font-bold">Filters</p>
      <div className="border p-2 px-2 border-zinc-200 mr-4 rounded my-4">
        <p className="text-lg font-bold">Department</p>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Computer Science & Engineering</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Business</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Mathetmatics</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Physics</p>
        </div>
      </div>
      <div className="border p-2 border-zinc-200 mr-4 rounded my-4">
        <p className="text-lg font-bold">Features</p>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Lecture Video</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Lecture Notes</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Practice Problems</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Slides</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Exams</p>
        </div>
      </div>
    </div>
  );
}
