/*
  Warnings:

  - A unique constraint covering the columns `[indicationTypeId,createdAt]` on the table `indications` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "indications_indicationTypeId_createdAt_key" ON "indications"("indicationTypeId", "createdAt");
